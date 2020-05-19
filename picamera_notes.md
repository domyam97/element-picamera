# Steps to Install PiCamera

* use pip to install picamera package  
* clone raspberrry pi userland and build with --aarch64 tag  
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
```#! /bin/sh  
sudo chown root:video /dev/vchiq  
sudo chmod g+rw /dev/vchiq```

`sudo chmod +x rc.local`  

* add yourself to video group

sudo usermod -a -G video $(whoami)





