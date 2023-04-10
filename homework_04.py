text = input("Enter a text: ")
if text.isdigit():
    print("This is a number.")
    if int(text) % 2 == 0:
        print ("The number is even.")
    else:
        print ("The number is odd.")
else:
    print(f"This is a word. It consists of {len(text)} letters.")

