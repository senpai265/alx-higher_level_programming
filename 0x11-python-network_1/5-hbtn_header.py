import requests
import sys

url = sys.argv[1]

try:
    response = requests.get(url)
    request_id = response.headers.get('X-Request-Id')
    
    if request_id:
        print(f"X-Request-Id: {request_id}")
    else:
        print("No X-Request-Id header found in the response")
        
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")

