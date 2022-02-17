# Code for the MongoDatabse

from dbi import DatabaseInterface
from typing import Dict, Tuple
from mongoengine import *
from mongo_ import Information
import json


class MongoDatabase(DatabaseInterface):
    database_name = "Tchami"

    def connect(self):
        reason = "-connecting to sql database"

        connect(self.database_name)
        print(f"connected to {self.database_name}")
        return True, reason

    def create(self, location: str, data: Dict[str, str]) -> Tuple[bool, str]:
        print(f"creating data in {location}")
        try:
            data_string = json.dumps(data)
            handle = Information(location=location, data=data_string)
            handle.save()
            reason = f"-Data created successfully in {location} location"
            print(reason)
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

            result = Information.objects()

            for contact in result:
                querier = (contact.data)
            reason = f"Data viewed successfully"
            print(reason)
            return True, reason, querier
        except Exception as k:
            reason = (
                f"Failed to read data in location {location}, reason: " + f"{type(k).__name__} {str(k)}")
            print(reason)
            return False, reason, ""

    def update(self, location: str, data: Dict[str, str]) -> Tuple[bool, str]:
        print(f"Updating data in {location} location")
        try:

            updater = Information.objects()
            print("Accesing "f"{location}")
            json_loader = json.dumps(data)
            updater.data = json_loader
            reason = f"-Data updated successful in location :{location}"
            print(reason)
            return True, reason

        except Exception as e:
            reason = (
                f"-Failed to update data in location {location}, reason: "
                + f"{type(e).__name__} {str(e)}"
            )
            print(reason)
            return False, reason

    def delete(self, location: str) -> Tuple[bool, str]:
        print(f"Deleting Contact in location {location}")
        try:
            result = Information.objects(location=location).first()
            #result_object = json.loads(result.data)
            result.delete()

            reason = f"Data Deleted Successfully"
            print(reason)
            return True, reason
        except Exception as e:
            reason = (
                f"-Failed to Delete data in location {location}, reason: "
                + f"{type(e).__name__} {str(e)}"
            )
            print(reason)
            return False, reason
