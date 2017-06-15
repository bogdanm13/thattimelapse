import os
import sys
from time import sleep

from picamera import PiCamera

WAIT_INIT = 5

class TimeLapser(PiCamera):

    def __init__(self, prefix, folder, wait, count=10, config={}):
        self.prefix = prefix
        self.folder = folder
        self.wait = wait
        self.count = count
        self.camera_config = config
        PiCamera.__init__(self)

    def prepare(self):
        os.makedirs(os.path.abspath(self.folder))
        
    def configure(self):
        # doing this after init since some of them do not work
        self.rotation = self.camera_config['rotation'] or 0

    def lapse(self):
        self.configure()
        self.start_preview()
        sleep(WAIT_INIT)
        for i in range(self.count):
            self.capture(os.path.join(self.folder, "{prefix}_{i}.jpg".format(prefix=self.prefix, i=i)))
            sleep(self.wait)
        self.stop_preview()


def main():
    tl = TimeLapser(prefix="timelapse", folder="capture/timelapse", wait=5, config={'rotation': 180})
    tl.lapse()


if __name__ == "__main__":
    sys.exit(main())