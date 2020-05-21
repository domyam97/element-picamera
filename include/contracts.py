from lazycontract import LazyContract, LazyProperty, FloatProperty, IntegerProperty
from atom.contracts import BinaryProperty, RawContract, EmptyContract

PICAMERA_ELEMENT_NAME = "picamera"

class ColorStreamContract(LazyContract):
        STREAM_NAME = "color"
        SERIALIZE = False

        data = BinaryProperty(required=True)
