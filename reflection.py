"""
This program mirrors an image:
first displays the original image, then displays the mirrored image on the horizontal axis.
"""

# Installs:
# python -m pip install PIllow

# Imports:
# first include simpleimage.py in the project folder
from simpleimage import SimpleImage

# Constants:
DEFAULT_FILE = 'images/mt-rainier.jpg'


def main():
    # Return original image
    filename = get_file()
    image = SimpleImage(filename)
    image.show()

    # Return mirrored image
    image = mirror_image(image)
    image.show()


def get_file():
    # Read image file path from user, or use the default file
    filename = DEFAULT_FILE # CHANGE THIS LATER input('Enter image file (or press enter for default): ')
    if filename == '':
        filename = DEFAULT_FILE
    return filename


def mirror_image(image):
    # Get dimensions of initial image for the for-loop_
    width = image.width
    height = image.height
    print(width, height)

    # Create a new image to place new pixels on top
    back_image = SimpleImage.blank(width, height * 2)

    # For-loop to paste pixels from imafe into back_image
    for x in range(width):
        for y in range(height):
            pixel = image.get_pixel(x, y)
            back_image.set_pixel(x, y, pixel)
            back_image.set_pixel(x, (height * 2) - (y + 1), pixel)

    return back_image


if __name__ == '__main__':
    main()