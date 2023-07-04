import requests
import sys

url = sys.argv[1]

try:
    response = requests.get(url)
    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")
    else:
        print(response.text)
    
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")

