index = int(input("Enter an index of a number in Fibonacci sequence: "))

def fibonacci_func(index):
    num1 = 0
    num2 = 1
    if index == 0:
        yield num1
    elif index == 1:
        yield num1
        yield num2
    elif index >= 2:
        yield num1
        yield num2
        for i in range(index - 1):
            num3 = num1 + num2
            num1 = num2
            num2 = num3
            yield num3

fibonacci_gen = fibonacci_func(index)

number = 0
for i in fibonacci_gen:
    number = i
print(number)

