from collections import UserDict

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return 'No record found with this name'
        except TypeError:
            return 'Please provide full info'

    return inner


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)
    
class Name(Field):
    def __init__(self, name):
        super().__init__(name)

class Phone(Field):
    def __init__(self, phone):
        super().__init__(phone)

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def edit_phone(self, old_phone, new_phone):
        for index, phone in enumerate(self.phones):
            if str(phone) == old_phone:
                self.phones[index] = Phone(new_phone)

    def find_phone(self, searched_phone):
        for phone in self.phones:
            if str(phone) == searched_phone:
                return str(phone)

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
    
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
        

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def hello():
    return 'How can I help you?'

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return 'Contact added.'

@input_error
def change_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return 'Contact updated.'

@input_error
def show_phone(args, contacts):
    name = args[0].lower()
    return contacts[name]

def show_all(contacts):
    result = ''
    for name, phone in contacts.items():
        result += f"{name.title()} {phone}\n"
    return result


def main():
    contacts = {}

    methods = {
        'hello': hello,
        'add': add_contact,
        'change': change_contact,
        'phone': show_phone,
        'all': show_all,
    }

    print('Welcome to the assistant bot!')

    while True:
        user_input = input('Enter a command:').strip().lower()
        command, *args = parse_input(user_input)

        if command in methods.keys():
            if command == 'hello':
                print(hello())
                continue

            if (len(args) > 0):
                print(methods[command](args, contacts))
            else:
                print(methods[command](contacts))
            continue

        if command in ['close', 'exit']:
            print("Good bye!")
            break

        print('Invalid command.')

if __name__ == "__main__":
    main()
