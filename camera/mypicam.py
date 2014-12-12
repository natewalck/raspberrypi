#!/usr/bin/python

import picamera
import time


def take_picture():
    current_time = time.strftime("%Y-%m-%d_%H.%M.%S")
    file_name = current_time + '.jpg'

    with picamera.PiCamera() as camera:
        camera.vflip = True
        camera.start_preview()
        time.sleep(2)
        camera.capture(file_name)

    return file_name


def main():
    print take_picture()


if __name__ == '__main__':
    main()