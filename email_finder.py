import re

text_file = input("File name: ")
with open(text_file, 'r') as file:
    text = file.read()

    print(re.findall(r'[a-zA-Z0-9_.]+@(?:[a-zA-Z0-9-]+\.)+[a-zA-z]{2,}', text)) # any other symbols relevant for email address can be added in []

    new_text = re.sub(r'[a-zA-Z0-9_.]+@(?:[a-zA-Z0-9-]+\.)+[a-zA-z]{2,}', '***@***', text)
    print(new_text)

    new_text2 = text
    emails_iter = re.finditer(r'[a-zA-Z0-9_.]+@(?:[a-zA-Z0-9-]+\.)+[a-zA-z]{2,}', new_text2)
    for item in emails_iter:
        email_to_replace = item.group()[1:-1]
        print(email_to_replace)
        new_text2 = re.sub(email_to_replace, '***@***', new_text2)

    print(new_text2)