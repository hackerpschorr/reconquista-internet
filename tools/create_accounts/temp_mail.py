from selenium import webdriver
import random
import time
from api import check_available


class TempMail:
    def __init__(self):
        profile = webdriver.FirefoxProfile()
        profile.set_preference('general.useragent.override',
                               'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1')
        self.driver = webdriver.Firefox(profile)
        self.driver.get('https://temp-mail.org/')

    def generate_email_address(self, name, surname):
        button_change = self.driver.find_element_by_id('click-to-change')
        button_change.click()
        time.sleep(2)

        user = name.lower() + random.choice('_-.') + surname.lower() + \
               random.choice('_-.') + str(random.randint(1000, 9999))

        form = self.driver.find_elements_by_tag_name('form')[0]
        input_user = form.find_element_by_id('mail')
        input_user.send_keys(user)
        form.submit()
        time.sleep(2)

        self.refresh()

        input_email = self.driver.find_element_by_id('mail')
        return input_email.get_attribute('value')

    def refresh(self):
        button_refresh = self.driver.find_element_by_id('click-to-refresh')
        button_refresh.click()
        time.sleep(2)

    def get_email(self):
        self.refresh()
        table = self.driver.find_element_by_id('mails')
        links = table.find_elements_by_class_name('title-subject')
        # open latest email
        links[0].click()
        time.sleep(2)

    def close(self):
        self.driver.close()


T = TempMail()
e = T.generate_email_address('anton', 'baumann')
print(e)
input("wait")
T.get_email()
T.close()

