#!/usr/bin/python

from flask import Flask, request
import mypicam

app = Flask(__name__)

@app.route('/', methods = ['POST'])
def index():
    data = request.get_data()
    if data == 'SECRET_HERE':
        mypicam.take_picture()
        print "Ok"
    else:
        print "Nope!"

    return("Done")


# Run
if __name__ == '__main__':
    app.run(
        host = "0.0.0.0",
        port = 5000
    )