from flask import Flask, request, jsonify 

server = Flask(__name__)
available_tickets = 20
version = 1

@server.get("/read")
def read_tickets():
    return jsonify(tickets = available_tickets, version=version)


@server.post("/write")
def write_tickets():
    global available_tickets
    booking = request.get_json()
    # locking
    if booking["version"] == version:
        available_tickets -= booking['num']
        print(booking)
        print(available_tickets)

        # relase the lock        return "successed"
    else:
        return "not success"


server.run(port=3000)
