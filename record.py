from name import Name
from phone import Phone

class Record:
    def __init__(self, name):
        try:
            self.name = Name(name)
        except ValueError as e:
            print(e)
        self.phones = []

    def add_phone(self, phone):
        try:
            self.phones.append(Phone(phone))
        except ValueError as e:
            print(e)

    def edit_phone(self, old_phone, new_phone):
        for index, phone in enumerate(self.phones):
            if str(phone) == old_phone:
                try:
                    self.phones[index] = Phone(new_phone)
                except ValueError as e:
                    print(e)

    def find_phone(self, searched_phone):
        for phone in self.phones:
            if str(phone) == searched_phone:
                return str(phone)

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
