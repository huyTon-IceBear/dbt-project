import os
import pandas as pd
import requests
import duckdb

# Preprocess the data frame based on the columns present.
def preprocess_dataframe(df):

    # For columns containing "Time", remove the unnecessary "0 days" part.
    for column in df.columns:
        if "Time" in column:
            df[column] = df[column].str.replace("0 days ", "")

    # For columns containing "LapTime", replace empty by 0 value.
    if 'LapTime' in df.columns:
        df['LapTime'] = df['LapTime'].apply(lambda x: '00:00:00.000000' if not x else x)

    return df

# Load data from a CSV file into duckdb.
def load_data_from_csv(conn, file_path):
    df = pd.read_csv(file_path)
    # Preprocess the data frame
    df = preprocess_dataframe(df)
    table_name = os.path.basename(file_path).replace(".csv", "")
    
   # Ensure the formula1 schema exists
    conn.execute("CREATE SCHEMA IF NOT EXISTS formula1")
    
    # Use DuckDB's from_df method, but also specify the schema "formula1"
    conn.from_df(df).create(f"formula1.{table_name}")

# Load data from a TXT file into duckdb.
def load_data_from_text(conn, file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    table_name = os.path.basename(file_path).replace(".txt", "")
    
   # Remove extra spaces from the beginning or end of lines then make a list.
    data = [{'line_content': line.strip()} for line in lines]

    df = pd.DataFrame(data)

    # Ensure the formula1 schema exists
    conn.execute("CREATE SCHEMA IF NOT EXISTS formula1")

    # Use DuckDB's from_df method, but also specify the schema "formula1"
    conn.from_df(df).create(f"formula1.{table_name}")

# Fetch data from given API endpoint.
def fetch_data_from_api(api_endpoint):
    response = requests.get(api_endpoint)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Failed to fetch data from {api_endpoint}")
        return None
    
# Load data from different sources (CSV files, TXT files, API) into duckdb.
def load_data_into_duckdb(conn, data_directory, api_base_url):
    data_files = os.listdir(data_directory)
    for file in data_files:
        file_path = os.path.join(data_directory, file)

        # Handle file format
        if file.endswith(".csv"):
            load_data_from_csv(conn, file_path)
        elif file.endswith(".txt"):
            load_data_from_text(conn, file_path)

    # Handle api endpoint
    drivers_api_endpoint = f"{api_base_url}/drivers"
    teams_api_endpoint = f"{api_base_url}/teams"

    drivers_data = fetch_data_from_api(drivers_api_endpoint)
    teams_data = fetch_data_from_api(teams_api_endpoint)

    if drivers_data:
        drivers_df = pd.DataFrame(drivers_data)
        conn.from_df(drivers_df).create("formula1.drivers")

    if teams_data:
        teams_df = pd.DataFrame(teams_data)
        conn.from_df(teams_df).create("formula1.teams")

def main():
    # Get the absolute path of the current script
    script_directory = os.path.dirname(os.path.abspath(__file__))
    
    # Set the data_directory relative to the script location (going up one directory level and then into the 'data' folder)
    root_directory = os.path.dirname(script_directory)  # Go up one level to the root
    data_directory = os.path.join(root_directory, "data")
    
    api_base_url = "http://localhost:3000"
    
    # Set db_path relative to the script location
    db_directory = os.path.join(root_directory, "dbt_formula1")
    db_path = os.path.join(db_directory, "database.duckdb")
    
    conn = duckdb.connect(database=db_path)
    load_data_into_duckdb(conn, data_directory, api_base_url)

if __name__ == "__main__":
    main()