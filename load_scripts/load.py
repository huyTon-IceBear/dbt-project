"""Script for loading data into DuckDB
"""
import duckdb

def main():
    """Main method, this is where the application starts.
       Currently there is an example given of how to work with DuckDB.
    """
    duckdb.sql('SELECT 43').show()

if __name__ == "__main__":
    main()
