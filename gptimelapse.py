from gopropyapi.goprocam import GoProCamera
from gopropyapi.goprocam import constants
import time
import datetime
from threading import Timer
import sys
import os
import config


class gpTimeLapse:
    gpCam = GoProCamera.GoPro()
    interval = int(config.GOPRO_CONFIG["interval"])  # seconds between shots

    def __init__(self):
        # redirect stdout to file
        # ref: https://stackoverflow.com/questions/11124093/redirect-python-print-output-to-logger/11124247
        directory = os.path.join(os.path.dirname(__file__), "log/")
        filename = "timelapse_" + str(time.time()) + ".log"
        if not os.path.exists(directory):
            os.makedirs(directory)
        path = os.path.join(directory, filename)
        print("Now going to redirect log output to file at ", path, " so going quiet - Bye bye!")
        log = open(path, "a")
        sys.stdout = log

    def take_photo(self):
        path = self.gpCam.take_photo(0)
        return path

    def run_timelapse(self):
        try:
            path = self.take_photo()
        except TypeError:
            print("Error, no camera found. Please connect to GoPro's wifi network first and try again!")
            return

        timestamp = time.time()
        formatted_time = datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')

        print(formatted_time, " captured photo and saved to ", path)
        Timer(self.interval, self.run_timelapse).start()
        print("start timer for ", self.interval)


if __name__ == '__main__':
    print("Running GPtimelapse... you must already be connected to the GoPro's built in WiFi for this to work")
    gpTimelapse = gpTimeLapse()
    gpTimelapse.run_timelapse()

