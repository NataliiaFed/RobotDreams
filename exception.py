from datetime import datetime

now = datetime.now()
current_time = now.strftime("%H:%M:%S")

class MyCustomException(Exception):
    def __init__(self, message):
        with open('error_logs.txt', 'a+') as f:  #'a' mode creates a file if it doesn't exist
            f.write(f'{current_time} {MyCustomException}: Custom exception is occured\n')

raise MyCustomException('Custom exception is occured')