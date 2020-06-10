# (Unofficial) GoPro Timelapse Control

**GoPro + Raspberry Pi = Timelapse**

This solution extends the built in functionality of the GoPro around capturing timelapse videos. This project runs on a device connected to your GoPro's wifi network can send commands to capture frames when you want them.  I used it on a Raspberry Pi 3B+ and GoPro Hero4 to record a construction timelapse, taking a photo every 10 minutes for 6 weeks straight. 

Useful added features:

* Longer intervals (>60 sec)

* Timelapse frames saved as still images to later combine together in Lightroom, LRTimelapse, etc. with greater customization


## Compatibility:
    HERO3
    HERO3+
    HERO4                 <--- Tested
    HERO4 Session
    HERO+
    HERO5 
    HERO5 Session
    HERO6
    Fusion 1
    HERO7 (Black)
    
    Raspberry Pi 3 Model A+
    Raspberry Pi 3 Model B       <--- Tested
    Raspberry Pi 3 Model B+   
    Raspberry Pi 4 Model B


## Getting started

### Raspberry Pi (RPi) Setup
 
* Flash RPi with Debian - [RPi docs](https://www.raspberrypi.org/documentation/installation/installing-images/) 
* Go through basic setup with raspi-config to set localization and wifi country
```pythonstub
# if it doesn't start automatically, can launch raspi-config from command line -
sudo raspi-config

# install pip3 and gopropy dependencies (this project uses Python3 due to the gopropy library)
sudo apt-get install python3-pip
pip3 install request

# Set static IP address in the default GoPro subnet 
#  TODO /etc/dhcpcd.conf

# Set wifi settings in wpa_supplicant file
# TODO: /etc/wpa_supplicant/wpa_supplicant.conf
```

_GoProControl App Setup_

* Clone this project 
* Edit config.py and set desired settings (interval, etc.)

_RPi Runtime Config_

* Edit ~/.bash_profile to launch the run script on startup
* Configure lxterminal to run on startup so it will start our script


### Quick Start

After going through RPI setup, turn GoPro WiFi setting on. Power up RPi and it will connect to the camera's WiFi and launch the timelapse script on bootup. 

Make sure the camera starts taking photos, and that's it!

Camera LEDs, sounds, and display can all be disabled in GoPro settings if desired.


### Accessories
Used a suction cup window mount - [link](https://www.amazon.com/gp/product/B01EF3Q8SU/ref=ppx_od_dt_b_asin_title_s00?ie=UTF8&psc=1). Suction held for about a week without falling.  Beyond that use painters tape or something for extra support.

Skeleton housing that allows camera to run with power cable connected - [link](https://www.amazon.com/gp/product/B00GLJBYRC/ref=ppx_od_dt_b_asin_title_s01?ie=UTF8&psc=1)


## Future improvements
 
* Set nested intervals, such as every 10 minutes between hours of 7am and 7pm each day
* Add screen and controls to see app state and start/stop.  The GoPro only allows one connection so cannot do this remotely.
 
## Dependencies
 
Python 3
[Unofficial GoPro API Library for Python](https://github.com/KonradIT/gopro-py-api)
 

 
 
