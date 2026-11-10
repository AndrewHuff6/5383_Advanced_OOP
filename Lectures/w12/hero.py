import requests

url = "http://localhost:5000/"

trials = 0
while True:
    number = int(input("Enter secret number: "))
    response = requests.post(url + "/api/guess", json={"secret": number})

    if response.text == "Success":
        print("Beaten the boss!")
        break

    trials += 1
    if trials >= 3:
        print("Boss wins!")
        break




    print(response.text)

