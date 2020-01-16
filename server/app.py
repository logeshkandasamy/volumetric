import json
import logging
import os
import time
import uuid
from datetime import datetime
import boto3
import decimal
from flask import Flask, request

app = Flask(__name__)

#Fetch from database
@app.route('/api/demo/<string:id>',methods=['GET'])
def read(id):
    print(id)
    return json.dumps({'id':id})


if __name__ == "__main__":
    app.run(port=8080)