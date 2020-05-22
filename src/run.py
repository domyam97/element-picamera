from time import sleep
from atom import Element
from atom.messages import Response, LogLevel
from picamera import PiCamera
from picamera.array import PiRGBArray
import numpy as np
import time
import cv2
from threading import Thread, Lock
import os 
import sys 

sys.path.append(os.path.abspath("/code/include"))

from contracts import ColorStreamContract, PICAMERA_ELEMENT_NAME

class Picamera:
    
    def __init__(self, element_name, width, height, fps, retry_delay):
        self._width = width
        self._height = height
        self._fps = fps
        self._retry_delay = retry_delay

        self._status_is_running = False
        self._status_lock = Lock()
        
        # Init element
        self._element = Element(element_name)
        self._element.healthcheck_set(self.is_healthy)
        #self._element.command_add(command_name, command_func_ptr, timeout, serialize)
        
        # Run command loop
        thread = Thread(target=self._element.command_loop, daemon=True)
        thread.start()
    
    def is_healthy(self):
        # Reports whether the camera is connected or not
        try:
           self._status_lock.acquire()
           if self._status_is_running:
               return Response(err_code=0, err_str="Camera is good")
           else:
               return Response(err_code=1, err_str="Camera is not good")
        except:
           return Response(err_code=0, err_str="Could not reach thread")

    def run_camera_stream(self):
        while True:
            try:
                # try to open up camera
                self._element.log(LogLevel.INFO, "Opening PiCamera")
                self._camera = PiCamera()
                self._color_array = PiRGBArray(self._camera)
                
                # set camera configs
                self._camera.resolution = (self._width, self._height)
                self._camera.framerate = self._fps
                
                # allow the camera to warm up
                time.sleep(.5)
                
                try:
                    self._status_lock.acquire()
                    self._status_is_running = True
                finally:
                    self._status_lock.release()
                
                self._element.log(LogLevel.INFO, "Picamera connected and streaming")
                
                while True:
                    start_time = time.time()
                    
                    self._camera.capture(self._color_array, format = 'bgr')
                    color_image = self._color_array.array
                    
                    #do some rotation here
                    
                    _, color_serialized = cv2.imencode(".tif", color_image)
                    
                    color_contract = ColorStreamContract(data=color_serialized.tobytes())
                    self._element.entry_write(
                            ColorStreamContract.STREAM_NAME,
                            color_contract.to_dict(),
                            serialize=ColorStreamContract.SERIALIZE,
                            maxlen=self._fps
                    )
                    time.sleep(max(1 / self._fps - (time.time() - start_time),0))
                    self._color_array.truncate(0)
            except:
                self._element.log(LogLevel.INFO, "Camera threw exception: %s" % (sys.exc_info()[1]))

            finally:
                try:
                    self._status_lock.acquire()
                    self._status_is_running = False
                    self._camera.close()
                finally: 
                    self._status_lock.release()

                time.sleep(self._retry_delay)

if __name__ == "__main__":
    element_name = os.getenv('ELEMENT_NAME', PICAMERA_ELEMENT_NAME)
    width  = int(os.getenv('WIDTH','1280'))
    height = int(os.getenv('HEIGHT','720'))
    fps = int(os.getenv('FPS','30'))
    rotation = os.getenv('ROTATION', None)
    retry_delay = float(os.getenv('RETRY_DELAY', '1.0'))
    
    if rotation is not None:
        try:
            rotation = int(rotation)
            if roation % 90 != 0:
                raise ValueError()
        except ValueError:
            raise ValueError("Rotation must be an integer that is a multiple of 90")
    
    camera = Picamera(
            element_name=element_name,
            width=width,
            height=height,
            fps=fps,
            retry_delay=retry_delay)
    
    camera.run_camera_stream()

