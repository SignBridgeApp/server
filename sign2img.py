from io import BytesIO
from signwriting.visualizer.visualize import signwriting_to_image
from PIL import Image


def to_bytes_io(image: Image) -> BytesIO:
    imgByte = BytesIO()
    image.save(imgByte, "png")
    imgByte.seek(0)
    return imgByte


def convert(fsw) -> BytesIO:
    print(fsw)
    img: Image = signwriting_to_image(fsw)
    return to_bytes_io(img)
