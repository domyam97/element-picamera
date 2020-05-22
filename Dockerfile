FROM elementaryrobotics/atom:opencv-aarch64

# Install sudo function
#RUN apt-get install sudo -y

# Lets copy over the contents of this repo into the container
#ADD ./third-party/userland /code/third-party/userland
ADD ./src /code

# install python dependencies
RUN pip3 install wheel
RUN pip3 install -r /code/requirements.txt

# try to compile userland
#WORKDIR /code/third-party/userland
#RUN chmod +x buildme
#RUN ./buildme --aarch64


ARG opt_libs
ENV PATH="/opt/vc/bin:${PATH}" 
RUN echo $PATH

ENV LD_LIBRARY_PATH="$opt_libs:${LD_LIBRARY_PATH}"
RUN echo $LD_LIBRARY_PATH

RUN ldconfig

WORKDIR /code
RUN chmod +x launch.sh
CMD ["/bin/sh", "launch.sh"]



