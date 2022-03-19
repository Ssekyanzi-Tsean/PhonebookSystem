import psycopg2
from config2 import config


class Psgql():
    params = config()
    print('Connecting to the postg ...')
    connection = psycopg2.connect(**params)

    crsr = connection.cursor()
    crsr.execute('''DROP TABLE IF EXISTS Information;CREATE
    UNLOGGED TABLE Information
      (location Serial PRIMARY KEY     NOT NULL,
      data           JSON    NOT NULL
      );''')

    def to_json(self):
        return {
            "location": self.location,
            "data": self.data
        }
    print("Table created successfully")

    connection.commit()
    connection.close()


if __name__ == "__main__":

    print("Creating Database")
