import requests


def check_available(email):
    url = 'https://api.twitter.com/i/users/email_available.json'
    params = {'email': email}
    return requests.request('get', url, params=params)


def register(email, password):
    url = 'https://api.twitter.com/1.1/onboarding/task.json'
    payload = {
        "flow_token": "g;152486754633500838:-1524867551571:989992381482225665:1",
        "subtask_inputs": [
            {
                "fetch_temporary_password": {
                    "link": "next_link",
                    "password": "c1f4b7f55f01ef73de75"
                },
                "subtask_id": "FetchTemporaryPassword"
            },
            {
                "enter_password": {
                    "link": "next_link",
                    "password": password
                },
                "subtask_id": "EnterPassword"
        }
    ]
}

s = check_available("test@test.de")
print(s)
