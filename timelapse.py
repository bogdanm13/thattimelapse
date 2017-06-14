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
    camera.rotation = 180
    tl = TimeLapser(camera)
    for i in range(10):
        tl.capture_image('/home/pi/Desktop/capture_%s.jpg' % i)

if __name__ == "__main__":
    sys.exit(main())