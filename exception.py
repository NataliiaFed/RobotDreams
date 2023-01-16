from datetime import datetime

now = datetime.now()
current_time = now.strftime("%H:%M:%S")

class MyCustomException(Exception):
    pass
# raise MyCustomException('Custom exception is occured')

try:
    raise MyCustomException('Test')
except MyCustomException:
    print(f'{current_time} {MyCustomException}: Custom exception is occured')