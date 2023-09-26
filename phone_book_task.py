def enter_name():
    return input('Contact name').capitalize()

def enter_surname():
    return input('Contact surname').capitalize()

def enter_phone_number():
    return input('Contact number')

def enter_adres():
    return input('Contact adress').capitalize()

def input_data():
    name = enter_name()
    surname = enter_surname()
    phnone_number = enter_phone_number()
    adress = enter_adres()

    with open('phone_book.txt', 'a', encoding='utf-8') as file:
        # print(file)
        file.write(f'{name} {surname}: {phnone_number}\n{adress}\n\n')

def print_data():
    with open('phone_book.txt', 'r', encoding='utf-8') as file:
        # print(file)
        print(file.read())

def search_line():
    search = input('Enter the search data: ').capitalize()
    with open('phone_book.txt', 'r', encoding='utf-8') as file:
        data = file.read().split('\n\n')[: -1]
        # print(data)
        for line in data:
            if search in line:
                print(line + '\n')
        # print(type(data))

def edit_contact():
    search = input('Enter the contact name or surname to edit: ').capitalize()
    with open('phone_book.txt', 'r', encoding='utf-8') as file:
        data = file.read().split('\n\n')[:-1]
    found = False

    with open('phone_book.txt', 'w', encoding='utf-8') as file:
        for line in data:
            if search in line:
                name, surname, rest = line.split(' ', 2)
                new_phone = input(f'Enter a new phone number for {name} {surname}: ')
                new_address = input(f'Enter a new address for {name} {surname}: ')
                file.write(f'{name} {surname}: {new_phone}\n{new_address}\n\n')
                found = True
            else:
                file.write(line + '\n')

def delete_contact():
    search = input('Enter the contact name or last name to delete: ').capitalize()
    with open('phone_book.txt', 'r', encoding='utf-8') as file:
        data = file.read().split('\n\n')[:-1]
    found = False

    with open('phone_book.txt', 'w', encoding='utf-8') as file:
        for line in data:
            if search in line:
                found = True
            else:
                file.write(line + '\n')

    if found:
        print('Contact deleted.')
    else:
        print('No contact found.')

def user_interface():
    choice = ''
    while choice != '6':
        print('''Select your action: 
                1 - Data entry
                2 - Output data
                3 - Search data
                4 - Data editing
                5 - Deletion of data
                6 - Exit''')
        choice = (input('Action number: '))
        
        while choice not in ('1', '2', '3', '4', '5', '6' ):
            print('INVAILD ENTRY')
            choice = (input('Action number: '))

            match(choice):
                case '1': input_data()
                case '2': print_data()
                case '3': search_line()
                case '4': edit_contact()
                case '5': delete_contact()
                case '6': print('Good bye!')


# print_data()
# search_line()
# input_data()
user_interface()