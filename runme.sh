#!/bin/bash

date >> output.log
whoami >> output.log
pwd >> output.log
FLASK_APP=app.py  FLASK_ENV=development  FLASK_DEBUG=1  /home/ubuntu/anaconda3/bin/flask  run  --port 8000  --host=0.0.0.0
