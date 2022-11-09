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
   return "<h1>Hello JewWithPenTest, "+hostname+", "+ipAddr+"</h1>"

@app.route('/f839c3a1-ec0f-4cc2-b97e-f8d981e9b4d5.html')
def uuidchecking():
   return ""

@app.route('/forti-uuid.html')
def uuidDetailCheck():
   return "<forti-uuid hidden>f839c3a1-ec0f-4cc2-b97e-f8d981e9b4d5</forti-uuid>"

if __name__ == '__main__':
 app.debug = True
 app.run(host='0.0.0.0', port=8000)
