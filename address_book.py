# AddressBook realization module
from collections import UserDict

class Field:
    """
    A base class representing a generic field with a value.
    """
    def __init__(self, value: str) -> None:
        """
        Initializes the Field with a given value.
        
        :param value: The value of the field as a string.
        """
        self.value = value

    def __str__(self):
        """
        Returns a string representation of the field's value.
        
        :return: String representation of the field's value.
        """
        return str(self.value)

class Name(Field):
    """
    Represents the name field of a contact. Inherits from Field.
    """
    pass  # Currently, no additional implementation is needed.

class Phone(Field):
    """
    Represents the phone number field of a contact. Inherits from Field.
    """
    pass  # Currently, no additional implementation is needed.

class Record:
    """
    Represents a contact record with a name and a list of phone numbers.
    """
    def __init__(self, name: str) -> None:
        """
        Initializes the Record with a name and an empty list of phone numbers.
        
        :param name: The name of the contact as a string.
        """
        self.name: Name = Name(name)
        self.phones: list[Phone] = []
        
    def is_phone_valid(self, phone: str) -> bool:
        """
        Checks if the given phone number is valid.
        A valid phone number is 10 digits long and numeric.
        
        :param phone: The phone number to check.
        :return: True if the phone number is valid, otherwise False.
        """
        return len(phone) == 10 and phone.isnumeric()
            
    def add_phone(self, phone: str) -> None:
        """
        Adds a phone number to the contact if it is valid.
        
        :param phone: The phone number to add.
        """
        if self.is_phone_valid(phone):
            self.phones.append(Phone(phone))
        
    def remove_phone(self, phone: str) -> None:
        """
        Removes a phone number from the contact if it exists.
        
        :param phone: The phone number to remove.
        """
        for index, p in enumerate(self.phones):
            if p.value == phone:
                del self.phones[index]
                break
                
    def edit_phone(self, old_value: str, new_value: str) -> None:
        """
        Edits an existing phone number with a new value if the new phone number is valid.
        
        :param old_value: The current phone number to be replaced.
        :param new_value: The new phone number to set.
        """
        if self.is_phone_valid(new_value):
            for index, p in enumerate(self.phones):
                if p.value == old_value:
                    self.phones[index] = Phone(new_value)
                    break
                
    def find_phone(self, phone: str) -> Phone:
        """
        Finds a phone number in the contact.
        
        :param phone: The phone number to find.
        :return: The Phone object if found, otherwise None.
        """
        for p in self.phones:
            if p.value == phone:
                return p
        return None
    
    def __str__(self) -> str:
        """
        Returns a string representation of the contact, including name and phone numbers.
        
        :return: String representation of the contact.
        """
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    """
    Represents an address book that stores multiple contact records.
    Inherits from UserDict to utilize dictionary-like functionality.
    """
    def add_record(self, record: Record) -> None:
        """
        Adds a record to the address book.
        
        :param record: The Record to add to the address book.
        """
        self.data.update({record.name.value: record})
        
    def find(self, name: str) -> Record:
        """
        Finds a record by the contact's name.
        
        :param name: The name of the contact to find.
        :return: The Record associated with the given name, or None if not found.
        """
        return self.data.get(name)
    
    def delete(self, name: str) -> None:
        """
        Deletes a record by the contact's name.
        
        :param name: The name of the contact to delete.
        """
        if name in self.data:
            self.data.pop(name)
            
            
# test part        
    
def test_field():
    field = Field("Test Value")
    assert str(field) == "Test Value"
    print("Field class test passed")

def test_record():
    record = Record("John Doe")
    assert str(record) == "Contact name: John Doe, phones: "
    record.add_phone("1234567890")
    assert "1234567890" in [p.value for p in record.phones]
    record.remove_phone("1234567890")
    assert "1234567890" not in [p.value for p in record.phones]
    record.add_phone("1234567890")
    record.edit_phone("1234567890", "0987654321")
    assert "0987654321" in [p.value for p in record.phones]
    assert not record.find_phone("1234567890")
    assert record.find_phone("0987654321").value == "0987654321"
    print("Record class test passed")

def test_address_book():
    address_book = AddressBook()
    record = Record("Jane Doe")
    address_book.add_record(record)
    assert address_book.find("Jane Doe") == record
    address_book.delete("Jane Doe")
    assert not address_book.find("Jane Doe")
    print("AddressBook class test passed")
    
# Uncomment code to run tests
# test_address_book()
# test_field()
# test_record()
