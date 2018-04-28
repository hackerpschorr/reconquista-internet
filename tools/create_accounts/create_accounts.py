from selenium import webdriver
import random
import string
import json
import re
from api import check_available

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
    email = name.lower() + random.choice('_-.') + surname.lower() + random.choice('_-.') + str(random.randint(1000, 9999))
    email = re.sub(r'[^\x00-\x7f]', r'', email)
    email += '@' + random_line_from_file(dict_path['provider'])
    return email if check_available(email)['valid'] else random_mail(name, surname)


def random_password(length):
    return ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits + "!@#$%^&*()_-+=?<>,.~") for _ in range(length))


def register():
    # generate data
    name, surname = random_name()
    data = {
        'name': '{} {}'.format(name, surname),
        'mail': random_mail(name, surname),
        'pass': random_password(16)
    }

    # set custom header
    profile = webdriver.FirefoxProfile()
    profile.set_preference('general.useragent.override',
                           'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1')

    # init driver with custom header
    driver = webdriver.Firefox(profile)

    try:
        # open twitter
        driver.get('https://mobile.twitter.com/signup?type=email')

        # first stage
        input_name = driver.find_element_by_id('oauth_signup_client_fullname')
        input_mail = driver.find_element_by_id('oauth_signup_client_phone_number')
        btn_submit = driver.find_element_by_name('commit')

        input_name.send_keys(data['name'])
        input_mail.send_keys(data['mail'])

        btn_submit.click()

        # second stage
        input_pass = driver.find_element_by_id('password')
        btn_submit = driver.find_element_by_name('commit')

        input_pass.send_keys(data['pass'])

        btn_submit.click()

        # third stage
        btn_submit = driver.find_element_by_xpath('/html/body/div/div[2]/div[3]/form/input')

        btn_submit.click()

        # fourth stage
        btn_submit = driver.find_element_by_name('commit')

        btn_submit.click()

        print(json.dumps(data))
        with open('accounts_2.jsonlst', 'a') as f:
            f.writelines(json.dumps(data) + '\n')

    finally:
        driver.close()


def main():
    while True:
        try:
            register()
        except:
            print("Change VPN")
            input("press ENTER")
            main()


if __name__ == '__main__':
    main()
