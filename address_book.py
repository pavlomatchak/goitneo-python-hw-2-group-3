from collections import UserDict

class AddressBook(UserDict):
    def __init__(self):
        self.data = {}
    
    def add_record(self, record):
        self.data[record.name.value] = record

    def delete(self, name):
        del self.data[name]

    def find(self,name):
        for key, record in self.data.items():
            if key == name:
                return record
