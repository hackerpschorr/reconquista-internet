from selenium import webdriver
import json
import argparse
import util

def register(args):
    # generate data
    name, surname = util.random_name()
    data = {
        'name': '{} {}'.format(name, surname),
        'mail': util.random_mail(name, surname),
        'pass': util.random_password(16)
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
        input_user = driver.find_element_by_id('custom_name')
        btn_submit = driver.find_element_by_name('commit')

        data['user'] = input_user.get_attribute('value')

        btn_submit.click()

        print(json.dumps(data))
        with open(args.output_file, 'a') as f:
            f.writelines(json.dumps(data) + '\n')

    finally:
        driver.close()


def main(args):
    while True:
        try:
            register(args)
        except Exception as e:
            print(e)
            print("Change VPN")
            input("press ENTER to continue.")
            main(args)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('output_file', help="specify output file", type=str)
    args = parser.parse_args()
    main(args)
