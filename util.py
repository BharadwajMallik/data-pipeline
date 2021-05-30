import pandas as pd
from mysql import connector as mc
from mysql.connector import errorcode
from config import db_details

def load_db_details(env):
    return db_details[env]


def get_mysql_connection(db_user,db_name,db_pass,db_host):
    try:
        conn=mc.connect(user=db_user,
                        host=db_host,
                        password=db_pass,
                        database=db_name)
    except mc.Error as error:
        if error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("invaid login details")
        else:
            print(error)

    return conn

def get_connection(db_type,db_host,db_name,db_user,db_pass):
    conn=None
    if db_type== 'mysql':
         conn=get_mysql_connection(db_host=db_host,
                                  db_name=db_name,
                                  db_user=db_user,
                                  db_pass=db_pass)
    elif db_type=='poatgres':
        # function not written for getting postgres connection
        conn=get_pg_connection(db_host=db_host,
                               db_name=db_name,
                               db_user=db_user,
                               db_pass=db_pass)
    return conn

def get_tables(path):
    tables=pd.read_csv(path, sep=':')
    return tables.query("to_be_loaded=='yes'")

