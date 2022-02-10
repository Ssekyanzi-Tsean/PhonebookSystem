import pytest
from phonebook import PhoneBookSystem
from filesystem import FileSystemDatabase
from sqlsystem import SqlDatabase
from unittest.mock import MagicMock, create_autospec, patch, Mock
from inmemory import InmemoryDatabase


# @pytest.mark.skip(reason="")
class TestPhoneBookSystem:
    #database_handle = FileSystemDatabase()
    #database_handle = InmemoryDatabase()
    database_handle = SqlDatabase
    phonebook_system = PhoneBookSystem(database_handle)

    def test_database_provider(self):
        # Prepare
        self.database_handle = FileSystemDatabase()
        self.phonebook_system = PhoneBookSystem(self.database_handle)
        self.phonebook_system.set_up_system()
        return None

    # @pytest.mark.skip(reason="")
    def test_create_contact(self):
        name = "Elsie"
        phone = "0788901797"
        data = {"name": name, "phone": phone}

        output = self.phonebook_system.create_contact(data)
        expected = (True, "Contact created Succesfully ")
        assert output == expected

    @pytest.mark.skip(reason="")
    def test_read_contact(self):
        name = "Elsie"
        phone = "0788901797"
        location = "0788901797"
        data = {"name": name, "phone": phone}
        self.phonebook_system.create_contact(data)
        output = self.phonebook_system.read_contact(data)
        excepted = (True, 'Contact read successfully', data)
        assert output == excepted

    @pytest.mark.skip(reason="")
    def test_update_contact(self):
        name = "Elsie"
        phone = "0788901797"
        data = {"name": name, "phone": phone}
        self.phonebook_system.create_contact(data)
        output = self.phonebook_system.update_contact(data)
        expected = (True, 'Contact updated successfully')
        assert output == expected

    @pytest.mark.skip(reason="")
    def test_delete_contact(self):
        name = "Elsie"
        phone = "0788901797"
        data = {"name": name, "phone": phone}
        self.phonebook_system.create_contact(data)
        output = self.phonebook_system.delete_contact(data)
        expected = (True, 'Contact deleted successfully')
        assert output == expected

    @pytest.mark.skip(reason="")
    def tear_down(self) -> None:
        self.phonebook_system.tear_down_system()
        return True
