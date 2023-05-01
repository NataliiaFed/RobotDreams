index = int(input("Enter an index of a number in Fibonacci sequence: "))

class Fibonacci:
    def __init__(self, max):
        self.max = max

    def __iter__(self):
        self.a = 0
        self.b = 1
        return self

    def __next__(self):
        fib = self.a
        if fib > self.max:
            raise StopIteration
        self.a, self.b = self.b, self.a + self.b
        return fib

fibonacci_itertor = Fibonacci(index)
for i in fibonacci_itertor:
    print(i)

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