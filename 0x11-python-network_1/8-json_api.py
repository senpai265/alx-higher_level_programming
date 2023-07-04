import requests
import sys

letter = sys.argv[1] if len(sys.argv) > 1 else ""
url = "http://0.0.0.0:5000/search_user"
data = {"q": letter}

try:
    response = requests.post(url, data=data)
    try:
        json_data = response.json()
        if json_data:
            print("[{}] {}".format(json_data.get("id"), json_data.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")

except requests.exceptions.RequestException as e:
    print("An error occurred:", e)

