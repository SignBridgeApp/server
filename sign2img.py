from io import BytesIO
from signwriting.visualizer.visualize import signwriting_to_image
from PIL import Image

def to_bytes_io(image: Image) -> bytes:
    imgByte = BytesIO()
    image.save(imgByte, "png")
    imgByte.seek(0)
    return imgByte.getvalue()

def convert(fsw: str, line_color=None, fill_color=None, arrangement="row") -> bytes:
    if not line_color or len(line_color) != 4:
        line_color = (0, 0, 0, 255)
    
    if not fill_color or len(fill_color) != 4:
        fill_color = (0, 0, 0, 0)
    
    fsw_list = fsw.split()

    # Convert each FSW string into an image and store them in a list
    images = []
    for fsw_string in fsw_list:
        img = signwriting_to_image(fsw_string, line_color=line_color, fill_color=fill_color)
        images.append(img)
    
    # Determine the maximum height and total width of all images
    max_height = max(img.height for img in images)
    total_width = sum(img.width for img in images)

    # Create a new image to hold all images either row-wise or column-wise
    if arrangement == "row":
        final_image = Image.new("RGBA", (total_width, max_height), (255, 255, 255, 0))
    elif arrangement == "column":
        final_image = Image.new("RGBA", (max_height, total_width), (255, 255, 255, 0))
    
    # Paste each image onto the final image either row-wise or column-wise
    x_offset = 0
    y_offset = 0
    for img in images:
        if arrangement == "row":
            final_image.paste(img, (x_offset, 0))
            x_offset += img.width
        elif arrangement == "column":
            final_image.paste(img, (0, y_offset))
            y_offset += img.height
    
    return to_bytes_io(final_image)
