from io import BytesIO
from signwriting.visualizer.visualize import signwriting_to_image
from PIL import Image


def to_bytes_io(image: Image) -> bytes:
    imgByte = BytesIO()
    image.save(imgByte, "png")
    imgByte.seek(0)
    return imgByte.getvalue()


def convert(fsw: str, line_color=None, fill_color=None) -> bytes:
    if not line_color or len(line_color) != 4:
        line_color = (0, 0, 0, 255)
    
    if not fill_color or len(fill_color) != 4:
        fill_color = (0, 0, 0, 0)
	
    img: Image = signwriting_to_image(fsw, line_color=line_color, fill_color=fill_color)
    return to_bytes_io(img)
