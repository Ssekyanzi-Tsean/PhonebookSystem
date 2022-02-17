# Run the Following Tags in the Terminal to Start Mongo Server
# Mongo start
# Mongo

# Code that creates the Fields(Tables)

from mongoengine import *


class Information(Document):
    location = StringField()
    data = StringField()

    def to_json(self):
        return {
            "location": self.location,
            "data": self.data
        }
