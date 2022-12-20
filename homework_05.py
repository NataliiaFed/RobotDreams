# TASK 1
text = input("Enter some text: ")
for char in text:
    if char.isdigit():
        char_int = int(char)
        if char_int % 2 == 0:
            print(f"{char} is a digit. It is an even number.")
        else:
            print(f"{char} is a digit. It is an odd number.")
    elif char.isalnum():
        if char.isupper():
            print(f"{char} is an uppercase letter.")
        else:
            print(f"{char} is a lowercase letter.")
    else:
        print(f"{char} is a symbol.")

# TASK 2
import time

while True:
    print("I love Python")
    time.sleep(4.2)