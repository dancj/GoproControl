# GoPro Timelapse Control

This projects extends the built-in timelapse capabilities of the GoPro by controlling the camera functions over the camera's built-in WiFi.
 
This may be a very specific use case, but I wanted to shoot a construction timelapse at 10 minute interval and my GoPro Hero4 Silver only supports up to 30 seconds. I needed a solution that allowed for:
 * Longer intervals (>60 sec)
 * Timelapse saved as still images to later combine together in Lightroom or LRTimelapse 

 
 ### Getting started
 
* Install Python 3.7, pip3
* Clone project 
* Edit config.py and set desired settings
* Run with `python gptimelapse.py`

 ### Suggested future improvements
 
 * Set nested intervals, such as every 10 minutes between hours of 7am and 7pm each day
 * Start up and connect to gopro wifi as soon as RPi powers on
 * Listen for commands to start and stop
 
 ### Dependencies
 
 This project uses the GoPro Python api made by Konrad Iturbe
 

 
 