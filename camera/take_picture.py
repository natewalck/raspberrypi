#!/usr/bin/python

import picamera
from time import sleep


def take_picture():
    file_name = 'test001.jpg'

    with picamera.PiCamera() as camera
        camera.vflip = True
        camera.start_preview()
        time.sleep(2)
        camera.capture(file_name)


def main():
    take_picture()


if __name__ == '__main__':
    main()