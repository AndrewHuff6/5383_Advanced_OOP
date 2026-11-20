import requests

def main():
    available_tickets = requests.get("/read").json()
    seats = available_tickets["available_tickets"]

    # time.sleep(10)

    if seats > 0:
        num_tickets = int(input("How many tickets you want: "))
        res = requests.post("http://127.0.0.1:3000/write", 
                    json={"num": num_tickets})

        # print(res)
        # print(res.status_code)


main()