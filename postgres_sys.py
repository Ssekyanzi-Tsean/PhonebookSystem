from multiprocessing import connection
from dbi import DatabaseInterface
from typing import Dict, Tuple
from sqldb import SqlDb
import json
import psycopg2
from config import config


class PostgresDatabase(DatabaseInterface):
    """Uses Postgresql as DBI"""
    connection = None

    def connect(self):

        reason = "-connecting to postgresql database"
        params = config()
        connection = psycopg2.connect(**params)
        crsr = connection.cursor()
        self.crsr = crsr()
        print("Postgres Database Version: ")
        crsr.execute('SELECT version()')
        db_version = crsr.fetchone()
        print(db_version)
        crsr.close()
