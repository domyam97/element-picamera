from time import sleep
from atom import Element
from atom.messages import Response

if __name__ == "__main__":
    element = Element("picamera")
    element.command_loop()

