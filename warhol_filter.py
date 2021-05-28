"""
Warhol effect
"""

# Installs:
# python -m pip install PIllow

# Imports:
# first include simpleimage.py in the project folder
from simpleimage import SimpleImage

# Constants:
DEFAULT_FILE = 'images/felix_the_cat.jpg'

CANVAS_ROWS = 2
CANVAS_COLS = 3


def main():
    # Import filename:
    filename = get_filename()
    image = SimpleImage(filename)

    # Get dimensions of the file and store them as variables:
    image_width = image.width
    image_height = image.height
    print(image_width, image_height)



def get_filename():
    filename = DEFAULT_FILE
    return filename


"""
    # Create a blank 3x2 canvas with the image:
    canvas = create_canvas(image, image_width, image_height)
    #canvas.show()

    # Apply the filter
    filtered_image = create_filter(canvas, image_width, image_height)
    filtered_image.show()


def create_canvas(image, image_width, image_height):
    canvas = SimpleImage.blank(image_width * CANVAS_COLS, image_height * CANVAS_ROWS, "white")
    for x in range(image_width):
        for y in range(image_height):
            pixel = image.get_pixel(x, y)
            for i in range(CANVAS_COLS):
                for j in range(CANVAS_ROWS):
                    canvas.set_pixel(x + (i * image_width), y + (j * image_height), pixel)

    return canvas


def create_filter(canvas, image_width, image_height):
    canvas_width = canvas.width
    canvas_height = canvas.height
    for x in range(canvas_width):
        for y in range(canvas_height):
            pixel = canvas.get_pixel(x, y)
            for i in range(CANVAS_COLS):
                for j in range(CANVAS_ROWS):
                    if 0 <= x <= image_width * (i+1) and 0 <= y <= image_height * (j+1):
                        if i == 0 and j == 0:
                            # pixel.red = 0
                             pixel.green = 0
                            # pixel.blue = 0
                        elif i == 1 and j == 0:
                            # pixel.red = 0
                            # pixel.green = 0
                             pixel.blue = 0
                        elif i == 2 and j == 0:
                            # pixel.red = 0
                             pixel.green = 0
                             pixel.blue = 0

    return canvas


"""


if __name__ == '__main__':
    main()