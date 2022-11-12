import socket
from flask import Flask

config = {
   "DEBUG": True
}
app = Flask(__name__)
app.config.from_mapping(config)

username="asdf"
pwd="zxcv@asdf"

@app.route('/')
def Home():
   hostname=socket.gethostname()
   ipAddr=socket.gethostbyname(hostname)
   return "<h1>Hello JewWithNewKey, "+hostname+", "+ipAddr+"</h1>"

@app.route('/89a54aa1-fbcf-4098-9304-e8f2ca551982.html')
def uuidchecking():
   return ""

@app.route('/forti-uuid.html')
def uuidDetailCheck():
   return "<forti-uuid hidden>89a54aa1-fbcf-4098-9304-e8f2ca551982</forti-uuid>"

if __name__ == '__main__':
 app.debug = True
 app.run(host='0.0.0.0', port=8000)
