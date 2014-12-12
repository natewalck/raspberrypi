#!/usr/bin/python

from flask import Flask, request
import mypicam
import os

app = Flask(__name__)

@app.route('/', methods = ['POST'])
def index():
    data = request.get_data()
    if data == 'SECRET_HERE':
        saved_pic = mypicam.take_picture()
        mypicam.upload_picture(saved_pic)
        os.remove(saved_pic)
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