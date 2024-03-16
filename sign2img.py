import io
from signwriting.visualizer.visualize import signwriting_to_image
from PIL import Image


def to_byte_array(image: Image) -> bytes:
    imgByteArr = io.BytesIO()
    image.save(imgByteArr, "png")
    imgByteArr = imgByteArr.getvalue()
    return imgByteArr


def convert(fsw):
    img: Image = signwriting_to_image(fsw)
    return to_byte_array(img)
