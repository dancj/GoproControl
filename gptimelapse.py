from gopropyapi.goprocam import GoProCamera
from gopropyapi.goprocam import constants
import time, datetime
from threading import Timer
import sys, os


class gpTimeLapse:
    # gpCam = GoProCamera.GoPro()
    interval = 10  # seconds between shots

    def __init__(self):
        # redirect stdout to file
        # ref: https://stackoverflow.com/questions/11124093/redirect-python-print-output-to-logger/11124247
        path = os.path.join(os.path.dirname(__file__), "log/timelapse_" + str(time.time()) + ".log")
        print("Now going to redirect log output to file at ", path, "- Bye bye!")
        log = open(path, "a")
        sys.stdout = log

    def take_photo(self):
        path = "test" # self.gpCam.take_photo(0)
        return path

    def run_timelapse(self):
        path = self.take_photo()

        timestamp = time.time()
        formatted_time = datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')

        print(formatted_time, " captured photo and saved to ", path)
        Timer(self.interval, self.run_timelapse).start()
        print("start timer for ", self.interval)


if __name__ == '__main__':
    print("Running timelapse...")
    gpTimelapse = gpTimeLapse()
    gpTimelapse.run_timelapse()

