# визначення числа в послідовності Фібоначчі, що відповідає прийнятому індексу:
index = int(input("Enter an index of a number in Fibonacci sequence: "))

# використовуючи генератори:
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

# використовуючи рекурсію:
def fibonacci_func(index):
    if index == 0:
        return 0
    elif index == 1:
        return 1
    return fibonacci_func(index-1) + fibonacci_func(index-2)

number = fibonacci_func(index)
print(number)


# знаходження факторіалу введеного числа, використовуючи рекурсію:
n = int(input("Enter a number to find its factorial: "))

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)
print(factorial(n))
