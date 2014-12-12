#!/usr/bin/python

import picamera
import time
import os
import subprocess

dropbox_uploader = '/home/pi/Dropbox-Uploader/dropbox_uploader.sh'
picture_path = '/tmp/'

def take_picture():
    current_time = time.strftime("%Y-%m-%d_%H.%M.%S")
    file_name = current_time + '.jpg'
    output_file = os.path.join(picture_path + file_name)

    with picamera.PiCamera() as camera:
        camera.vflip = True
        camera.resolution = (1280, 960)
        camera.start_preview()
        time.sleep(2)
        camera.capture(output_file)

    return output_file


def upload_picture(pic_path):
    subprocess.call([dropbox_uploader, 'upload', pic_path, '.'])


def main():
    saved_pic = take_picture()
    upload_picture(saved_pic)
    os.remove(saved_pic)


if __name__ == '__main__':
    main()