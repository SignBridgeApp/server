from io import BytesIO
from signwriting.visualizer.visualize import signwriting_to_image
from PIL import Image


def to_bytes_io(image: Image) -> BytesIO:
    imgByte = BytesIO()
    image.save(imgByte, "png")
    imgByte.seek(0)
    return imgByte


def convert(fsw: str, line_color=None) -> BytesIO:
    if not line_color or len(line_color) != 4:
        line_color = (0, 0, 0, 255)

    img: Image = signwriting_to_image(fsw, line_color=line_color, embedded_color=True)
    return to_bytes_io(img)
