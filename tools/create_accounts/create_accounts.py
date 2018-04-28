from selenium import webdriver
import random
import string

dict_path = {
    'names': 'lists/names.lst',
    'surnames': 'lists/surnames.lst',
    'provider': 'lists/email_provider.lst'
}

dict_length = {
    'names': 20561,
    'surnames': 3421,
    'provider': 3618
}


def random_line_from_file(path):
    lines = open(path).read().splitlines()
    return random.choice(lines)


def random_name():
    name = random_line_from_file(dict_path['names'])
    surname = random_line_from_file(dict_path['surnames'])
    return name, surname


def random_mail(name, surname):
    email = name.lower() + random.choice("_-.") + surname.lower() + random.choice("_-.") + str(random.randint(1000, 9999))
    email += '@' + random_line_from_file(dict_path['provider'])
    return email


def random_password(length):
    return ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(length))


def main():
    # set custom header
    profile = webdriver.FirefoxProfile()
    profile.set_preference("general.useragent.override", "Mozilla/5.0 (Windows NT 6.1; rv:27.3) Gecko/20130101 Firefox/27.3")

    # init driver with custom header
    driver = webdriver.Firefox(profile)

    # open twitter
    driver.get("https://twitter.com/signup?lang=de")

    # find inputs
    input_name = driver.find_element_by_id("full-name")
    input_mail = driver.find_element_by_id("email")
    input_pass = driver.find_element_by_id("password")

    # generate data
    name, surname = random_name()
    data = {
        'name': '{} {}'.format(name, surname),
        'mail': random_mail(name, surname),
        'pass': random_password(16)
    }

    print(data)

    # fill inputs
    input_name.send_keys(data['name'])
    input_mail.send_keys(data['mail'])
    input_pass.send_keys(data['pass'])

    # submit form
    input_pass.submit()

    # driver.close()


if __name__ == '__main__':
    main()

