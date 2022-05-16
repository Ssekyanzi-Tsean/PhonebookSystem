from config import DATABASE_URI
import os
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, String, DateTime, Integer, create_engine, Date


BASE_DIR = os.path.dirname(os.path.realpath(__file__))
connection_string = "sqlite:///"+os.path.join(BASE_DIR, 'migrant.db')

Base = declarative_base()

engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)
s = Session()


class Phonedb(Base):

    __tablename__ = 'information'

    location = Column(String, primary_key=True)
    data = Column(String)


if __name__ == "__main__":
    Base = declarative_base()
    print("Postgres Db Connected")