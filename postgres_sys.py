from multiprocessing import connection
from dbi import DatabaseInterface
from typing import Dict, Tuple
from postgres_db import Psgql
from sqldb import SqlDb
import json
import psycopg2
from config2 import config


class PostgresDatabase(DatabaseInterface):
    """Uses Postgresql as DBI"""
    params = config()
    connection = psycopg2.connect(**params)
    #connection = None

    def connect(self):

        reason = "-connecting to postgresql database"
        #self.connection = connection
        crsr = self.connection.cursor()
        self.crsr = crsr
        print("Postgres Database Version: ")
        crsr.execute('SELECT version()')
        db_version = crsr.fetchone()
        print(db_version)
        crsr.close()
        return True, reason

    def disconnect(self):
        reason = "-Disconnecting from postgresql database"
        return True, reason

    def create(self, location: str, data: Dict[str, str]) -> Tuple[bool, str]:
        """creates data """
        print(f"creating data in {location} ")
        try:
            data_string = json.dumps(data)
            handle = self.connection.cursor()
            handle.execute(
                "INSERT INTO Information VALUES (%s, %s);", (location, data_string))
            self.connection.commit()
            print("Record Inserted Succesfully")
            self.connection.close()
            reason = f"-Data created successfully in {location} location"
            print(reason)
            return (True, reason)
        except Exception as e:
            reason = (
                f"Failed to create data in location {location}, reason: " + f"{type(e).__name__} {str(e)}")
            print(reason)
            return(False, reason)

    def read(self, location: str) -> Tuple[bool, str, Dict[str, str]]:
        """Reads in data in system"""
        print(f"-Reading data in {location} location")
        row = []
        try:

            conn_curs = self.connection.cursor()
            conn_curs.execute("SELECT * FROM Information")
            result = self.cursor.fetchall()
            result_object = json.loads(result.data)
            for resultant in result_object:
                print("Contact:{0}".format(resultant))
            reason = f"Data viewed successfully"
            print(reason)
            return True, reason, result_object
        except Exception as k:
            reason = (
                f"Failed to read data in location {location}, reason: " + f"{type(k).__name__} {str(k)}")
            print(reason)
            return False, reason, ""
