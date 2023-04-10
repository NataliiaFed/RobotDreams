class Bot:

    def __init__(self, name):
        self.name = name

    def say_name(self):
        print(self.name)

    def send_message(self, message):
        print(message)


class TelegramBot(Bot):

    def __init__(self, name):
        super().__init__(name)
        self.url = None
        self.chat_id = None

    def set_url(self, url):
        self.url = url

    def set_chat_id(self, chat_id):
        self.chat_id = chat_id

    def send_message(self, message):
        print(f"{self.name} bot says {message} to chat {self.chat_id} using {self.url}")


some_bot = Bot('Nata')
some_bot.say_name()
some_bot.send_message("Hello")

telegram_bot = TelegramBot("TG")
telegram_bot.say_name()
telegram_bot.send_message('Hello')
telegram_bot.set_chat_id(1)
telegram_bot.send_message('Hello')

# =================================================================================
class MyStr(str):

    def __str__(self):
        return self.upper()

my_str = MyStr('test')
print(my_str)

# =================================================================================
class User:

    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name.lower() == other.name.lower()

first_user = User('NATALIIA')
second_user = User('Nataliia')
print(first_user == second_user)

# =================================================================================
def init_function(self, name):
    self.name = name

def say_name_function(self):
    print(self.name)

def send_message_function(self, message):
    print(message)

new_bot_class = type(
    'SecondBot',
    (),
    {
        '__init__' : init_function,
        'say_name' : say_name_function,
        'send_message' : send_message_function
    }
)
another_bot = new_bot_class('Nata')
another_bot.say_name()
another_bot.send_message("Hello")


def set_url_function(self, url):
    self.url = url

def set_chat_id_function(self, chat_id):
    self.chat_id = chat_id

def send_message_function(self, message):
    print(f"{self.name} bot says {message} to chat {self.chat_id} using {self.url}")

new_telegrambot_class = type(
    'SecondTelegramBot',
    (new_bot_class, ),
    {
        '__init__' : init_function,
        'set_url' : set_url_function,
        'set_chat_id' : set_chat_id_function,
        'send_message' : send_message_function,
        'url' : None,
        'chat_id' : None
    }
)

another_telegram_bot = new_telegrambot_class("TG")
another_telegram_bot.say_name()
another_telegram_bot.send_message('Hello')
another_telegram_bot.set_chat_id(1)
another_telegram_bot.send_message('Hello')