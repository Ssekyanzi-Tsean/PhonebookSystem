import pytest
import phonebook
from phonebook import PhoneBookSystem
from dbi import DatabaseInterface
from filesystem import FileSystemDatabase
from sqlsystem import SqlDatabase
from unittest.mock import MagicMock, create_autospec, patch, Mock
from inmemory import InmemoryDatabase
from unittest import mock
from unittest.mock import MagicMock, create_autospec, patch, Mock



class TestPhoneBookSystem:
    #database_handle = FileSystemDatabase()
    #database_handle = InmemoryDatabase()
    database_handle = SqlDatabase
    phonebook_system = PhoneBookSystem(database_handle)

    # def test_database_provider(self):
    #     # Prepare
    #     self.database_handle = FileSystemDatabase()
    #     self.phonebook_system = PhoneBookSystem(self.database_handle)
    #     self.phonebook_system.set_up_system()
    #     return None

    # @pytest.mark.skip(reason="")
    def test_create_contact(self):
        database_handle = MagicMock()
        database_handle = InmemoryDatabase()
        phonebook_system = PhoneBookSystem(database_handle)
        name = "Elsie"
        phone = "0788901797"
        data = {"name": name, "phone": phone}
        location = "0788901797"
        output = self.phonebook_system.create_contact(data)
        expected = (True, "Contact created Succesfully ")
        assert output == expected

    # @pytest.mark.skip(reason="")

    
    def test_read_contact(self):
        #Prepare
        database_handle = MagicMock()
        database_handle = InmemoryDatabase()
        phonebook_system = PhoneBookSystem(database_handle)
        name = "Andrew"
        phone = "0772129076"
        data = {"name": name, "phone": phone}

        
        phonebook_system.create_contact(data)
       
        output = phonebook_system.read_contact(data)
        excepted = (True, 'Contact read successfully', data)
        assert output == excepted

    
    def test_update_contact(self):
        #Prepare
        database_handle = MagicMock()
        database_handle = InmemoryDatabase()
        phonebook_system = PhoneBookSystem(database_handle)
        name = "Elsie"
        phone = "0788901797"
        data = {"name": name, "phone": phone}
        phonebook_system.create_contact(data)
        output = phonebook_system.update_contact(data)
        expected = (True, 'Contact updated successfully')
        assert output == expected

    
    def test_delete_contact(self):
        database_handle = InmemoryDatabase()
        phonebook_system = PhoneBookSystem(database_handle)
        name = "Elsie"
        phone = "0788901797"
        data = {"name": name, "phone": phone}
        phonebook_system.create_contact(data)
        output = phonebook_system.delete_contact(data)
        expected = (True, 'Contact deleted successfully')
        assert output == expected

    #@pytest.mark.skip(reason="")
    def test_tear_down(self) -> None:
        database_handle = InmemoryDatabase()
        phonebook_system = PhoneBookSystem(database_handle)
        output = phonebook_system.tear_down_system()
        expected = "System shut down complete"
        assert output == expected
