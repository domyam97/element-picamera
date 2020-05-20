FROM elementaryrobotics/atom:opencv-aarch64

# Install sudo function
RUN apt-get install sudo cmake build-essential -y

# Lets copy over the contents of this repo into the container
ADD ./third-party/userland /code/third-party/userland
ADD . /code

# install python dependencies
RUN pip3 install wheel
RUN pip3 install picamera[array]

# try to compile userland
WORKDIR /code/third-party/userland
RUN chmod +x buildme
RUN ./buildme --aarch64

RUN export PATH=$PATH:/opt/vc/bin && echo $PATH
#RUN export LD_LIBRARY_PATH=$LD_LIBRARY_PATH/opt/vc/lib && echo $LD_LIBRARY_PATH

RUN ldconfig

WORKDIR /code
RUN chmod +x launch.sh
CMD ["/bin/bash", "launch.sh"]



