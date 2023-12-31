import string

from faker import Faker

base_url = "https://b2c.passport.rt.ru"

# Валидные данные:
valid_email = "wet05956@zslsz.com"
valid_password = 'B/#-ds4wS3Mg-GK'
valid_firstname = "Эрнесто"
valid_lastname = "Чегевара"
valid_login = "Romario"
valid_region = "Москва"


# Невалидные данные:
random = Faker()

# Случайный пароль:
random_password = random.password()
# Случайный адрес электронной почты:
random_email = random.email()

invalid_ls = "269750005232"
invalid_login = "invalid_login"
invalid_phone = "+79211234567"


def generate_cyrillic_string(n):
    return 'я' * n


def generate_english_string(n):
    return "s" * n


def english_chars():
    return 'qwertyuiopasdfghjklzxcvbnm'


def cyrillic_chars():
    return 'абвгдеёжзиклмнопрстуфхцчшщъыьэюя'


def special_chars():
    return f'{string.punctuation}'


def japanese_symbols():
    return '原千五百秋瑞'


def chinese_symbols():
    return '龍門大酒家'
