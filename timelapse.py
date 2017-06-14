import sys
from time import sleep

from picamera import PiCamera


class TimeLapser(object):

    def __init__(self, camera):
        self.camera = camera

    def capture_image(self, path):
        self.camera.start_preview()
        sleep(5)
        self.camera.capture(path)
        self.camera.stop_preview()


def main():
    camera = PiCamera()
    tl = TimeLapser(camera)
    tl.capture_image('/home/pi/Desktop/capture.jpg')

if __name__ == "__main__":
    sys.exit(main())