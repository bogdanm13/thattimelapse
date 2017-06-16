import argparse
import os
import sys
from time import sleep

from picamera import PiCamera

WAIT_INIT = 5


class TimeLapser(PiCamera):

    def __init__(self, prefix, folder, wait, count=10, config={}):
        self.prefix = prefix
        self.folder = os.path.abspath(folder)
        self.wait = wait
        self.count = count
        self.camera_config = config
        PiCamera.__init__(self)

    def prepare(self):
        os.makedirs(self.folder, exist_ok=True)

    def configure(self):
        # doing this after init since some of them do not work
        self.rotation = self.camera_config['rotation'] or 0

    def lapse(self):
        self.prepare()
        self.configure()
        self.start_preview()
        sleep(WAIT_INIT)
        for i in range(self.count):
            self.capture(os.path.join(self.folder, "{prefix}_{i}.jpg".format(prefix=self.prefix, i=i)))
            sleep(self.wait)
        self.stop_preview()


def get_args():
    argparser = argparse.ArgumentParser()
    argparser.add_argument('-p', '--prefix', default='timelapse',
                           help="The prefix of the image's name")
    argparser.add_argument('-d', '--destination', default='capture/timelapse',
                           help='The folder where to save the images')
    return argparser.parse_args()


def main():
    args = get_args()
    tl = TimeLapser(prefix=args.prefix, folder=args.destination, wait=5, config={'rotation': 180})
    tl.lapse()


if __name__ == "__main__":
    sys.exit(main())