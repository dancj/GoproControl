from gopropyapi.goprocam import GoProCamera
from gopropyapi.goprocam import constants
import time


class gpTimeLapse:
    gpCam = GoProCamera.GoPro()

    def take_photo(self):
        path = self.gpCam.take_photo(0)
        return path


if __name__ == '__main__':
    print("Running timelapse...")
    gpTimelapse = gpTimeLapse()
    gpTimelapse.take_photo()

