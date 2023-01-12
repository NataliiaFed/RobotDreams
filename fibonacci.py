# визначення числа в послідовності Фібоначчі, що відповідає прийнятому індексу:
index = int(input("Enter an index of a number in Fibonacci sequence: "))

# використовуючи генератори:
def fibonacci_func(range_num):
    num1 = 0
    num2 = 1
    for i in range(range_num):
        yield num1
        num1, num2 = num2, num1 + num2

fibonacci_list = list(fibonacci_func(index+1)) # range_num = index + 1
print(fibonacci_list[index])

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