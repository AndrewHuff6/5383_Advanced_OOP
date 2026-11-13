import requests

url = "http://localhost:5000/"

trials = 0
while trials <= 4:
    number = int(input("Enter secret number: "))
    response = requests.post(url + "/api/guess", json={"secret": number})

    if response.text == "Success":
        print("Beaten the boss!")
        break

    trials += 1
  




print("Boss wins!")
        




    #print(response.text)

