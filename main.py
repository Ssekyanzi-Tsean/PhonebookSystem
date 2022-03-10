from filesystem import FileSystemDatabase
from phonebook import PhoneBookSystem
from inmemory import InmemoryDatabase
from sqlsystem import SqlDatabase
from mongosystem import MongoDatabase
from postgres_sys import PostgresDatabase

#database_service = FileSystemDatabase()
#database_service = InmemoryDatabase()
#database_service = MongoDatabase()
#database_service = SqlDatabase()
database_service = PostgresDatabase()

phonebook_system = PhoneBookSystem(database_service)
phonebook_system.set_up_system()


name = "Sean"
name2 = "Ssekyanzi"
phone = "0701901797"
phone2 = "0788901797"


#phonebook_system.create_contact({"name": name, "phone": phone})
#print(phonebook_system.read_contact({"name": name, "phone": phone}))
#phonebook_system.update_contact({"name": name2, "phone": phone})
#phonebook_system.delete_contact({"name": name2, "phone": phone})
