#!/usr/bin/python

import picamera
import time
import os

def take_picture(pic_path):
    current_time = time.strftime("%Y-%m-%d_%H.%M.%S")
    file_name = current_time + '.jpg'
    os.path.join(pic_path + file_name)

    with picamera.PiCamera() as camera:
        camera.vflip = True
        camera.start_preview()
        time.sleep(2)
        camera.capture(file_name)

    return file_name


def main():
    picture_path = '/tmp/'
    print take_picture(picture_path)


if __name__ == '__main__':
    main()