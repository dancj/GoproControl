from gopropyapi.goprocam import GoProCamera
from gopropyapi.goprocam import constants
import time


def start_timelapse():
    gpCam = GoProCamera.GoPro()
    print gpCam.take_photo(1)


if __name__ == '__main__':
    print "Hello"
