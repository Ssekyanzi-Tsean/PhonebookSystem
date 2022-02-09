# Phonebook Code
from dbi import DatabaseInterface
from typing import Dict, Tuple


class PhoneBookSystem:
    """PhoneBook Implemantation"""

    def __init__(self, db_service_provider: DatabaseInterface) -> None:
        """Creates a db provider instance"""
        self.db = db_service_provider

    def set_up_system(self) -> None:
        print("Starting up system")
        self.db.connect()
        print("System startup complete")

    def create_contact(self, data: dict) -> Tuple[bool, str]:
        print("Creating contact")
        try:
            phone = data["phone"]

            created, reason = self.db.create(phone, data)
            if not created:
                reason = "failed to create contact"
                print(reason)
            return False, reason
        except Exception:
            reason = "Contact created Succesfully "
            print(reason)
            return True, reason

    def read_contact(self, data: dict) -> Tuple[bool, str, Dict[str, str]]:
        print("Viewing contact information")
        location = data["phone"]

        read, reason, output = self.db.read(location)
        if not read:
            reason = "failed to read contact"
            print(reason)
            return False, reason, ""

        reason = "Contact read successfully"
        print(reason)
        return True, reason, data

    def update_contact(self, data: Dict[str, str]) -> Tuple[bool, str]:
        """Update method """
        print("Updating contact")
        phone = data["phone"]
        print(phone)
        updated, reason = self.db.update(phone, data)
        print(reason)
        if not updated:
            print(reason)
            reason = "failed to update contact"
            return False, reason

        reason = "Contact updated successfully"
        print(reason)
        return True, reason

    def delete_contact(self, data: Dict[str, str]) -> Tuple[bool, str]:
        print("Deleting contact information")

        phone = data["phone"]
        deleted, reason = self.db.delete(phone)

        if not deleted:
            print(reason)
            reason = "failed to delete contact"
            return False, reason

        reason = "Contact deleted successfully"
        print(reason)
        return True, reason

    def tear_down_system(self) -> None:
        print("Shutting down system")
        self.db.disconnect()
        print("System shut down complete")
