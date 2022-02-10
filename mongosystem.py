# Code for the MongoDatabse

from dbi import DatabaseInterface
from typing import Dict, Tuple
from mongoengine import *


class MongoDatabase(DatabaseInterface):
    database_name = "Tchami"

    def connect(self):
        reason = "-connecting to sql database"

        connect(self.database_name)
        print(f"connected to {self.database_name}")
        return True, reason
