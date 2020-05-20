# Steps to Install PiCamera

This is a way to get PiCamera up and running locally, outside the docker container. Most of this stuff is reused in the Docker container. 

## Prerequisites
Can be installed with apt:
* build-essential package (C++ compiler and some build tools)
* cmake

You need a 64-bit OS - I recommend [Ubuntu Server for Raspberry Pi](https://ubuntu.com/download/raspberry-pi) with your choice of desktop environment.  
*In order to run on a RPi3 with it's limited RAM you might need to play around with Desktop Managers and Display Managers*

## Install Steps
* use pip to install picamera package  
* clone [Raspberrry Pi Userland](https://github.com/raspberrypi/userland) and build with --aarch64 tag  
* add all the stuff you built to your path  

`touch ~/.bash_aliases`  
`echo -e 'PATH=$PATH:/opt/vc/bin\nexport PATH' >> ~/.bash_aliases`   
`echo -e 'LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/vc/lib\nexport LD_LIBRARY_PATH' >> ~/.bash_aliases`   
`source ~/.bashrc`  
`sudo ldconfig`  
`sudo reboot now`  

* create an /etc/rc.local script to change vchiq file permissions on boot

`touch /etc/rc.local`  
`vim /etc/rc.local`  

Your rc.local file should look like this:  
```  
#! /bin/sh  
sudo chown root:video /dev/vchiq  
sudo chmod g+rw /dev/vchiq
```  
Make your new rc.local runnable
`sudo chmod +x rc.local`  

* add yourself to video group

`sudo usermod -a -G video $(whoami)`





