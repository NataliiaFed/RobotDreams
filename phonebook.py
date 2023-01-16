import json
# ============================================================
# Переносимо телефонну книгу з python-файлу в новий json-файл:
phonebook = {
    'Anna':'+111111111',
    'Bogdan':'+222222222',
    'Vova':'+333333333',
    'Gena':'+444444444'
}

json_phonebook = json.dumps(phonebook)

try:
    with open("phonebook.json", 'x') as f:
        f.write(json_phonebook)
except FileExistsError:
    print('File "phonebook.json" already exists')

# ============================================================
# Завантажуємо дані з існуючого json-файлу для роботи з ними:
with open("phonebook.json", 'r') as f:
    json_phonebook = f.read()

phonebook = json.loads(json_phonebook)
print(phonebook)

command = ''
while command != 'exit':
    command = input("Enter a command stats/add/delete/list/show or exit: ")

    match command:
        case 'stats': # stats: кількість записів
            key_list = phonebook.keys()
            print(len(key_list))

        case 'add': # add: додати запис
            name = input("Enter a name: ")

            if name in phonebook:
                print("Contact with this name already exists.")
            else:
                phonenumber = input("Enter a phone number: ")
                phonebook[name] = phonenumber

                json_phonebook = json.dumps(phonebook)
                with open("phonebook.json", 'w') as f:
                    f.write(json_phonebook)

        case 'delete': # delete <name>: видалити запис за іменем (ключем)
            name = input("Enter a name: ")

            try:
                del phonebook[name]
            except KeyError:
                print(f"Contact '{name}' is not found.")
            else:
                print(f"Contact '{name}' is deleted.")

                json_phonebook = json.dumps(phonebook)
                with open("phonebook.json", 'w') as f:
                    f.write(json_phonebook)

        case 'list': # list: список всіх імен в книзі
            key_list = phonebook.keys()
            print(key_list)

        case 'show': # show <name>: детальна інформація по імені
            name = input("Enter a name: ")
            print(phonebook.get(name))

        case 'exit':
            exit()