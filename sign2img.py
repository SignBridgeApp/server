from signwriting.visualizer.visualize import signwriting_to_image
from PIL import Image


def convert(fsw):
	img:Image = signwriting_to_image(fsw)
	return img.tobytes()
