import requests

url = "https://alx-intranet.hbtn.io/status"

response = requests.get(url)
response_body = response.text

# Display the body of the response with tabulation before each line
formatted_body = "\n".join(["\t" + line for line in response_body.split("\n")])
print(formatted_body)

