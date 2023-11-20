# We import a method from the  modules to address environment variables and 
# we use that method in a function that will return the variables we need from .env 
# to a dictionary we call sql_config

from dotenv import dotenv_values
import sqlalchemy
import pandas as pd
from sqlalchemy import create_engine


def get_sql_config():
    '''
        Function loads credentials from .env file and
        returns a dictionary containing the data needed for sqlalchemy.create_engine()
    '''
    needed_keys = ['host', 'port', 'database','user','password', 'db_url']
    #needed_keys = ['host', 'port', 'database','password', 'db_url']

    dotenv_dict = dotenv_values(".env")
    sql_config = {key:dotenv_dict[key] for key in needed_keys if key in dotenv_dict}
    return sql_config



# get_data() function definition 
def get_data(sql_query, schema_name = 'muc_dp_23_1', *args, **kwargs):

    ''' Connect to the PostgreSQL database server, run query and return data'''
    # get the connection configuration dictionary using the get_sql_config function
    
    sql_config_data = get_sql_config()

    # create a connection engine to the PostgreSQL server

    engine = create_engine('postgresql://user:pass@host/database',
                        connect_args= {
                            'host': sql_config_data['host'], 
                            'port' : sql_config_data['port'],
                            'database': sql_config_data['database'],
                            #'user' : sql_config_data['user'],
                            'password' : sql_config_data['password']                        
                        } # use dictionary with config details
                        )
    # open a conn session using 'with', execute the query, and return the results

    with engine.begin() as conn: 
        results = conn.execute(sql_query)
        print(results.fetchall())



# function definition for get_connection_engine and get_dataframe() using read_sql_query()
# - call the function imported get_sql_config() and save the results to a variable
# - function to get connection engine to database
# - get data from database using the engine and an sql query

def get_connengine(db_url):

    sql_config_data = get_sql_config()

    # create a connection engine to the PostgreSQL server

    if engine!=None:
        try:

            engine = create_engine(db_url)
        except (Exception, sqlalchemy.exc.SQLAlchemyError) as error:
            print(error)
            engine = None
    else:
        print('No engine')

    return engine

def get_conn_engine():

    # get database url, db_url

    sql_config_data = get_sql_config()

    db_url = f'''postgresql://{sql_config_data['user']}:{sql_config_data['password']}@{sql_config_data['host']}:{sql_config_data['port']}/{sql_config_data['database']}'''

    # create a connection engine to the PostgreSQL server

    try:
        engine = create_engine(db_url)
    except (Exception, sqlalchemy.exc.SQLAlchemyError) as error:
        print(error)

    return engine


def get_dataframe(sql_query, conn_engine):
    ''' 
    Connect to the PostgreSQL database server, 
    run query and return data as a pandas dataframe
    '''
    moosic_data = pd.read_sql_query(sql=sql_query, con=conn_engine)

    return moosic_data