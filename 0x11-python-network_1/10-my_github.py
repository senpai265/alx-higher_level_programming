import requests
import sys

username = sys.argv[1]
access_token = sys.argv[2]

url = "https://api.github.com/user"
headers = {"Authorization": f"Basic {username}:{access_token}"}

try:
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        user_data = response.json()
        user_id = user_data.get("id")
        print(f"Your GitHub user id is: {user_id}")
    else:
        print(f"Error: {response.status_code} - {response.text}")

except requests.exceptions.RequestException as e:
    print("An error occurred:", e)

