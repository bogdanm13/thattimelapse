import os
import sys
from time import sleep

from picamera import PiCamera


class TimeLapser(PiCamera):

    def __init__(self, folder, wait, count=10, config={}):
        self.folder = folder
        self.wait = wait
        self.count = count
        self.camera_config = config

    def configure(self):
        # doing this after init since some of them do not work
        self.rotation = self.camera_config['rotation']

    def lapse(self):
        self.start_preview()
        self.configure()
        sleep(5)
        for i in range(self.count):
            self.capture(os.path.join(self.folder, 'capture_%s.jpg' % i))
            sleep(self.wait)
        self.stop_preview()


def main():
    tl = TimeLapser("/home/pi/Desktop", 5, config={'rotation':180})
    tl.lapse()


if __name__ == "__main__":
    sys.exit(main())