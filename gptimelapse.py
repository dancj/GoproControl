from gopropyapi.goprocam import GoProCamera
from gopropyapi.goprocam import constants
import time, datetime
from threading import Timer
import sys


class gpTimeLapse:
    gpCam = GoProCamera.GoPro()
    interval = 10  # seconds between shots

    def __init__(self):
        # redirect stdout to file
        # ref: https://stackoverflow.com/questions/11124093/redirect-python-print-output-to-logger/11124247
        log = open("timelapse_" + time.time() + ".log", "a")
        sys.stdout = log

    def take_photo(self):
        path = self.gpCam.take_photo(0)
        return path

    def run_timelapse(self):
        path = self.take_photo()

        timestamp = time.time()
        formatted_time = datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')

        print(formatted_time, " captured photo and saved to ", path)
        Timer(self.interval, self.run_timelapse).start()


if __name__ == '__main__':
    print("Running timelapse...")
    gpTimelapse = gpTimeLapse()
    gpTimelapse.take_photo()

