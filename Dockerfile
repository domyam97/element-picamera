FROM elementaryrobotics/atom:opencv-aarch64

# Install sudo function
RUN apt-get install sudo cmake build-essential -y

# Lets copy over the contents of this repo into the container
ADD ./third-party/userland /code/third-party/userland
ADD . /code

# install python dependencies
RUN pip3 install wheel
RUN pip3 install picamera[array]

# add a docker user

# RUN useradd -m docker && echo "docker:docker" | chpasswd && adduser docker sudo && adduser docker video
# RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

# USER docker


WORKDIR /code

RUN chmod +x launch.sh

# try to compile userland
RUN chmod +x third-party/userland/buildme
RUN third-party/userland/buildme --aarch64

CMD ["/bin/bash", "launch.sh"]



