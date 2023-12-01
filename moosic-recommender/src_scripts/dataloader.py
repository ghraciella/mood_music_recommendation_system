"""
script : data_processing.py 
purpose: 


"""


# Importing necessary libraries and modules 

import subprocess

try:

    import numpy as np
    import pandas as pd
    import random as rnd

    # databases - sql
    import psycopg2
    import sqlalchemy
    from dotenv import dotenv_values, load_dotenv
    from sqlalchemy import create_engine

    # data - api
    import requests

    # object serialisation
    import pickle
    import joblib

    # pipeline
    from sklearn.pipeline import Pipeline
    from sklearn.pipeline import make_pipeline

    # custom imports
    from .sql_functions import get_sql_config


except ImportError as error:
    print(f"Installation of the required dependencies necessary! {error}")

    subprocess.check_call(["pip", "install", "numpy"])
    subprocess.check_call(["pip", "install", "pandas"])
    subprocess.check_call(["pip", "install", "psycopg2-binary"])
    subprocess.check_call(["pip", "install", "python-dotenv"])
    subprocess.check_call(["pip", "install", "pickle"])
    subprocess.check_call(["pip", "install", "joblib"])
    subprocess.check_call(["pip", "install", "requests"])


    print(f"Successful installation of the required dependencies necessary")


import warnings
warnings.filterwarnings('ignore')




# functions
# - get data from csv or parquet or excel file
# - get data from saved vector or embedded file formats : pkl , joblib, npy
# - get data from api
# - get data from postgres database
# - get data from data vault or datalake or data warehouse 
# - get data from datalake on cloud 
# - data cleaning and transformation function
# - saving data as vectors or embedding to be used later
# - separate function that does all the above using pyspark and orchestrating with airflow 






def get_data_structured_file(data_path, *args, **kwargs):
    """
    function to map and read data based on their file formats
    tabular and structured data file formats

    supported file formats: 
        'csv' - csv, 'parquet' - parquet, 
        'xlsx' or 'xls' -  excel, 'json' - json
        
    """

    read_functions = {
        'csv': pd.read_csv,
        'xlsx': pd.read_excel,
        'json': pd.read_json,
        'parquet': pd.read_parquet,
        'xls': pd.read_excel,
        
    }

    get_file_extension = data_path.split('.')[-1].lower()

    if get_file_extension not in read_functions:
        raise ValueError(f"Unsupported file format: {get_file_extension}")

    try:
        read_function = read_functions[get_file_extension]
        data = read_function(data_path)
        return data
    except Exception as error:
        print(f"Error reading file: {error}")
        return None




def get_data_serialized_file(data_path, *args, **kwargs):
    """
    function to map and read data based on their file formats
    
    supported file formats: 
        'pkl' - pickle, 'joblib' - joblib
        'npy' - numpy, 'txt' - text
        
    """


    get_file_extension = data_path.split('.')[-1].lower()

    try:
        if get_file_extension == 'pkl':
            with open(data_path, 'rb') as f:
                data = pickle.load(f)

        elif get_file_extension == 'joblib':
            with open(data_path, 'rb') as f:
                data = joblib.load(f)

        elif get_file_extension == 'npy':
            data = np.load(data_path, allow_pickle=True)

        else:
            raise ValueError(f"Unsupported file format: {get_file_extension}")
        
        return data
    except Exception as error:
        print(f"Error reading file: {error}")
        return None




def get_conn_engine_alchemy(driver=None, *args, **kwargs):

    """
    SQLAlchemy - function to create a connection to the PostgreSQL server

    - call the function imported get_sql_config() which gets the credentials
    - use the configurations gotten to create the database connection string (db_url)
        - with no specific driver (automatic choice based on environment configurations and installed packages) 
        - or with psycopg2 driver (PostgreSQL adapter)
    - return engine
        
    """

    sql_config_data = get_sql_config()

    if driver == 'psycopg2':
        db_url = f'''postgresql+psycopg2://{sql_config_data['user']}:{sql_config_data['password']}@{sql_config_data['host']}:{sql_config_data['port']}/{sql_config_data['database']}'''

    else:
        db_url = f'''postgresql://{sql_config_data['user']}:{sql_config_data['password']}@{sql_config_data['host']}:{sql_config_data['port']}/{sql_config_data['database']}'''


    try:
        engine = create_engine(db_url)
        print("Connection Sucessful!")
    except (Exception, sqlalchemy.exc.SQLAlchemyError) as error:
        print(error)

    return engine


def get_conn_engine_psycopg(query, *args, **kwargs):

    """
    psycopg2 driver (PSQL adapter) - function to create a connection to the PostgreSQL server

    - call the function imported get_sql_config() which gets the credentials
    - use the configurations gotten to create the database connection 
    - return engine / connection object
    
    """

    sql_config_data = get_sql_config()

    try:
        engine = psycopg2.connect(
            user=sql_config_data['user'],
            password=sql_config_data['password'],
            host=sql_config_data['host'],
            database=sql_config_data['database']
        )
        print("Connection Sucessful!")
    except (Exception, psycopg2.Error) as error:
        print(error)

    return engine



def get_data_postgres_db(sql_query, conn_engine, driver=None, *args, **kwargs):
    ''' 
    Get data using connection engine to connect to the PostgreSQL database server, 

    psycopg2 :
        - execute sql queries with a curser for the connection
        - call execute() method on cursor
        - use of fetchall() to fetch all rows from executed query
        - close cursor and connection
        - return data as a pandas dataframe

    else :
        - takes query and connection engine
        - read query using pandas method read_sql_query()
        - return data as a pandas dataframe

    '''

    if driver == 'psycopg2':

        con = conn_engine
        cursor = con.cursor()
        cursor.execute(sql_query)
        data = cursor.fetchall()
        cursor.close()
        con.close()
        data = pd.DataFrame(data)

    else:
        data = pd.read_sql_query(sql=sql_query, con=conn_engine)

    return data 




def get_data_apis(url, *args, **kwargs):
    ''' 
    Get data from API

    param: url  


    '''

    response = requests.get(url)
    data = response.json()

    return data 










