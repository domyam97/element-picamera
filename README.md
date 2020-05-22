# element-picamera
An AtomOS Element for use with the Raspberry Pi Camera Modules. 
It is intended as a low cost way for users to get set up with computer vision within Elementary Robotics' AtomOS.

## Prerequisites
This docker container is meant to run on a RPi3B+ or RPi4. 
This is becuase the AtomOS has been cross compiled for a 64 bit ARM system like these Raspberry Pi's or the NVIDIA Jetson Series.
In order to run the AtomOS software we first need to install a 64-bit OS. I recommend [Ubuntu Server 20.04 for the Raspberry Pi](https://ubuntu.com/download/raspberry-pi) with your choice of OS.  
You'll also need a PiCamera of course. Anything from the original V1 to __maybe__ the new Raspberry Pi High Quality Camera module.

## Software you'll need
* Docker
*   There are lots of guides for installing docker. Most of them should work for the Raspberry Pi. I recommend using snap, which comes ready to go on Ubuntu Server. 
* docker-compose

## Installation
First please read the picamera_notes.md and get all your drivers installed locally.
I'm working on getting all those steps into a script so you won't have to worry about all that.

I'm also working on getting an image on Docker Hub. So for now, clone this repo and run  
`docker-compose up`  
This compose file runs the picamera element and a streamviewer element so you can watch your stream live.  
In general, element-picamera will publish images to the picamera:color redis stream.     
Once it's built you can enter the container and start playing around.  
`docker exec -it element-picamera bash`  
### Preinstalled Python Libraries

These are all available in the container.

* OpenCV `cv2`  
* picamera + picamera[array]
* numpy

I'm also working on getting this to stream to element-streamviewer from elementary robotics as a default test application. 
This will also mean we're publishing images to an image stream so you can play around with more elements in AtomOS.  
Try to build your own camera drone or UGV! Or maybe just an IOT Security camera!

Check out the [Atom Docs](atomdocs.io) for more on AtomOS.

 
