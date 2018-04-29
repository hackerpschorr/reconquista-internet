import requests


def check_available(email):
    url = 'https://api.twitter.com/i/users/email_available.json'
    params = {'email': email}
    r = requests.get(url, params=params)
    return r

