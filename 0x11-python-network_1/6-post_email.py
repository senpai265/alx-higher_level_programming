import requests
import sys

url = sys.argv[1]
email = sys.argv[2]

data = {'email': email}

try:
    response = requests.post(url, data=data)
    print(response.text)
    
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")

