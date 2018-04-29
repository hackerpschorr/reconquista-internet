import random
import re
import string
from api import check_available

dict_path = {
    'names': 'lists/names.lst',
    'surnames': 'lists/surnames.lst',
    'provider': 'lists/email_provider.lst'
}


def random_line_from_file(path):
    lines = open(path).read().splitlines()
    return random.choice(lines)


def random_name():
    name = random_line_from_file(dict_path['names'])
    surname = random_line_from_file(dict_path['surnames'])
    return name, surname


def random_mail(name, surname):
    email = name.lower() + random.choice('_-.') + surname.lower() + random.choice('_-.') + str(random.randint(1000, 9999))
    email = re.sub(r'[^\x00-\x7f]', r'', email)
    email += '@' + random_line_from_file(dict_path['provider'])
    return email if check_available(email).json()['valid'] else random_mail(name, surname)


def random_password(length):
    return ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits + "!@#$%^&*()_-+=?<>,.~") for _ in range(length))
