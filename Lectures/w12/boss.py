import requests

url = "http://localhost:5000/"

number = int(input("Enter secret number: "))
response = requests.post(url + "/api/set_secret", json={"secret": number})

print(response.text)
print(response)