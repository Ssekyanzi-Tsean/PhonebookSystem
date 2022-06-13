from filesystem import FileSystemDatabase
from phonebook import PhoneBookSystem
from inmemory import InmemoryDatabase
from sqlsystem import SqlDatabase
from mongosystem import MongoDatabase
from post_alc_usage import PostgresDatabase


#database_service = FileSystemDatabase()
#database_service = InmemoryDatabase()
#database_service = MongoDatabase()
#database_service = SqlDatabase()
database_service = PostgresDatabase()


phonebook_system = PhoneBookSystem(database_service)
phonebook_system.set_up_system()


name = "Sean"
name2 = "Tchami"
name3 = "james"

phone = "0701901797"
phone2 = "0788901797"
phone3 = "0735653612"


phonebook_system.create_contact({"name": name2, "phone": phone2})
#print(phonebook_system.read_contact({"name": name3, "phone": phone}))
#phonebook_system.update_contact({"name": name3, "phone": phone})
#phonebook_system.delete_contact({"name": name3, "phone": phone})
