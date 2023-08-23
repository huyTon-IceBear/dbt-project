# Retake OLAP template
This manual is based on using Python/DuckDB/dbt from a unix-based terminal. This means you have to use MacOS, Linux (Ubuntu, CentOS, Debian, ...) or WSL on Windows.

## Structure
This project consists of the following folders:
- **api**: contains the API with driver and team information. See `README.md` in folder for more information.
- **data**: contains all the data files that should be loaded in your DuckDB database.
- **load_scripts**: should contain your Python/NodeJS files for loading data into a DuckDB database.
- **dbt_formula1**: contains the dbt project. Don't forget to configure the project for you own database (see `profile.yml`).

## Installation
There are multiple programming languages allowed for loading data into DuckDB. You can decide for yourself which language you want to use. We recommend using Python or NodeJS. For the dbt part you will have to use python (to run the dbt command). Please read the following Python installation instructions. If you want to use NodeJS, we advice you to install nvm (https://github.com/nvm-sh/nvm) and use Node version 16.x.x.

### Installing Python
1. Install `python3` and `python3-pip` on your system (with APT/brew or another package manager).
2. Run the command `pip install poetry` or `pip3 install poetry` to install the package and dependency manager Poetry (see https://python-poetry.org/).
3. Browse to the root of your project and run `poetry install` to install all dependencies for this project.

## Running the application

### Loading data with Python
Start your loading scripts with `poetry run python3 load_scripts/load.py`

### Running DBT
Make sure Python is installed and your poetry dependencies are installed. You can execute the dbt commands using poetry by running: `poetry run dbt run` from the `dbt_formula1` folder

### Running DuckDB
Make sure Python is installed and your poetry dependencies are installed. You can execute DuckDB using poetry as well: `poetry run duckdb <database_filename>`.