# 1. Написати власний декоратор, задачею якого має бути друк назви функції і часу, коли вона була викликана.
from datetime import datetime

now = datetime.now()
current_time = now.strftime("%H:%M:%S")

def my_decorator(func):
    def deco_func(*args, **kwargs):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print(f"Function name: {func}")
        print(f"Function call time: {current_time}")
        result = func(*args, **kwargs)
        return result
    return deco_func

@my_decorator
def multiply(a, b):
    return a * b

print(multiply(3.55, 7.63))

# ===============================================================================================
# 2. Написати кастомний Exception клас, MyCustomException, який має повідомляти "Custom exception is occured"

class MyCustomException(Exception):
    pass

# raise MyCustomException('Custom exception is occured')

# коли перехоплюємо помилку:
try:
    raise MyCustomException('Test')
except MyCustomException:
    print('Custom exception is occured')

# ===============================================================================================
# 3. Написати власний менеджер контексту, задачею якого буде друкувати "==========" – 10 знаків дорівнює
# перед виконанням коду та після виконання коду, таким чином виділяючи блок коду символами дорівнює.
# У випадку виникнення будь-якої помилки вона має бути надрукована текстом, проте програма не має завершити своєї роботи.

class MyManager:
    def __enter__(self):
        print('='*10)
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print(f"Exception: {exc_val}")
        print('=' * 10)
        return True

with MyManager():
    # print("Hello!")
    print(a)

# ===============================================================================================
# 4. Написати конструкцію try ... except ... else ... finally, яка буде робити точно те ж,
# що і менеджер контексту із попереднього завдання.

try:
    print('=' * 10)
    print("Hello!")
    # print(a)
except Exception as e:
    print(f"Exception: {e}")
else:
    print("The code is correct.")
finally:
    print('=' * 10)