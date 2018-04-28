import requests


def check_available(email):
    url = 'https://api.twitter.com/i/users/email_available.json'
    params = {'email': email}
    r = requests.request('get', url, params=params)
    return r.json()
