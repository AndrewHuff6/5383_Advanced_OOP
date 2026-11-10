# be sure to pip install flask before running 
from flask import Flask, request

server = Flask(__name__)
secret = None
num_tries = 0
game_over = False

@server.route('/api/get_state', methods=['GET'])
def get_state():
    return "Hello World"

@server.route('/api/set_secret', methods=['POST'])
def set_secret():
    global secret
    x = request.get_json()
    print(x)
    secret = x["secret"]
    return "Success"

@server.route('/api/guess', methods=['POST'])
def guess():
   data = request.get_json()
   num = data["secret"]
   if num == secret:
       return "Correct!"
   else:
       return "Try again!"

server.run(port=5000, threaded=False)