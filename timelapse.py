import os
import sys
from time import sleep

from picamera import PiCamera

WAIT_INIT = 5

class TimeLapser(PiCamera):

    def __init__(self, folder, wait, count=10, config={}):
        self.folder = folder
        self.wait = wait
        self.count = count
        self.camera_config = config
        PiCamera.__init__(self)

    def configure(self):
        # doing this after init since some of them do not work
        self.rotation = self.camera_config['rotation']

    def lapse(self):
        self.configure()
        self.start_preview()
        sleep(WAIT_INIT)
        for i in range(self.count):
            self.capture(os.path.join(self.folder, 'capture_%s.jpg' % i))
            sleep(self.wait)
        self.stop_preview()


def main():
    tl = TimeLapser("/home/pi/Desktop", 5, config={'rotation':180})
    tl.lapse()


if __name__ == "__main__":
    sys.exit(main())