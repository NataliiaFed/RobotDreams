# Створити телефонну книгу,
phonebook = {
    'Anna':'+111111111',
    'Bogdan':'+222222222',
    'Vova':'+333333333',
    'Gena':'+444444444'
}

# яка матиме команди:
command = ''
while command != 'exit':
    command = input("Enter a command stats/add/delete/list/show or exit: ")
    match command:
        case 'stats': # stats: кількість записів
            key_list = phonebook.keys()
            print(len(key_list))
        case 'add': # add: додати запис
            name = input("Enter a name: ")
            phonenumber = input("Enter a phone number: ")
            phonebook[name] = phonenumber
            print(phonebook)
        case 'delete': # delete <name>: видалити запис за іменем (ключем)
            name = input("Enter a name: ")
            del phonebook[name]
            print(phonebook)
        case 'list': # list: список всіх імен в книзі
            key_list = phonebook.keys()
            print(key_list)
        case 'show': # show <name>: детальна інформація по імені
            name = input("Enter a name: ")
            print(phonebook.get(name))