import os
from os.path import join, dirname

from dotenv import load_dotenv
import mysql.connector

dotenv_path = join(dirname(__file__), '.env.local')
load_dotenv(dotenv_path)

config = {
    'user': os.getenv('USER'),
    'password': os.getenv('PASS'),
    'host': os.getenv('HOST'),
    'port': os.getenv('PORT'),
    'database': os.getenv('DATABASE'),
    'raise_on_warnings': True
}


def with_connection(f):
    def with_connection_(*args, **kwargs):
        conn = mysql.connector.Connect(**config)
        try:
            result = f(*args, connection=conn, **kwargs)
        except:
            conn.rollback()
            print("SQL failed")
            raise
        else:
            conn.commit()
        finally:
            conn.close()
        return result
    return with_connection_