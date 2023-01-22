from datetime import datetime

now = datetime.now()
current_time = now.strftime("%H:%M:%S")

def my_decorator(func):
    def deco_func(*args, **kwargs):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        with open('logs.txt', 'a+') as f:  #'a' mode creates a file if it doesn't exist
            f.write(f"Function name: {func} Call time: {current_time}\n")
        result = func(*args, **kwargs)
        return result
    return deco_func

@my_decorator
def multiply(a, b):
    print(a * b)

multiply(3, 7)