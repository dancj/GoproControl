# GoPro Timelapse Control

This projects extends the built-in timelapse capabilities of the GoPro by controlling the camera functions over the camera's built-in WiFi.  The GoPro can broadcast its own WiFi network that will accept one connection.  This may be a very specific use case, but I wanted to shoot a construction timelapse at 10 minute interval and my GoPro Hero4 Silver only supports up to 30 second intervals. 

I needed a solution that allowed for:
 * Longer intervals (>60 sec)
 * Timelapse saved as still images to later combine together in Lightroom or LRTimelapse 

There are certainly cheaper cameras for this project, but if you already have a GoPro why not make use of it.
 
## Getting started

#### Environment Setup
 
1. Set up raspberry pi with Debian - [docs](https://www.raspberrypi.org/documentation/installation/installing-images/) 
1. Go through basic setup with raspi-config to set localization and wifi country
1. Install pip3 (this project uses Python3 due to the GoPro library)
    ```
    sudo apt-get install python3-pip
    pip3 install request
    ```
1. Set static IP address 
    ``` /etc/dhcpcd.conf ```
1. Set wifi settings in wpa_supplicant file
    ``` /etc/wpa_supplicant/wpa_supplicant.conf ```

#### App Setup

1. Clone this project 
1. Edit config.py and set desired settings (interval, etc.)

#### Runtime Config

1. Edit ~/.bash_profile to launch the run script on startup
1. Configure lxterminal to run on startup so it will start our script

## Hardware
Used a suction cup window mount - [link](https://www.amazon.com/gp/product/B01EF3Q8SU/ref=ppx_od_dt_b_asin_title_s00?ie=UTF8&psc=1)
* the suction held for about a week without falling.  Beyond that use painters tape or something for extra support.
Skeleton housing that allows camera to run with power cable connected - [link](https://www.amazon.com/gp/product/B00GLJBYRC/ref=ppx_od_dt_b_asin_title_s01?ie=UTF8&psc=1)

### Tested configuration
* GoPro Hero 4 Silver
* Raspberry Pi 3 Model B

## Future improvements
 
* Set nested intervals, such as every 10 minutes between hours of 7am and 7pm each day
* Add screen and controls to see app state and start/stop.  The GoPro only allows one connection so cannot do this remotely.
 
## Dependencies
 
This project uses the [Unofficial GoPro API Library for Python](https://github.com/KonradIT/gopro-py-api)
 

 
 