"""
This program implements a rad image filter.
"""
# Installs:
# python -m pip install PIllow

# Imports:
# first include simpleimage.py in the project folder
from simpleimage import SimpleImage

# Constants:
DEFAULT_FILE = 'images/mario_star.png'


def main():
    # Get file and load image
    filename = get_file()
    image = SimpleImage(filename)

    # Show the image before the transform
    image.show()

    # Apply the filter
    jmage = apply_filter(image)

    # Show the image after the transform
    image.show()


def get_file():
    # Read image file path from user, or use the default file
    filename = input('Enter image file (or press enter for default): ')
    if filename == '':
        filename = DEFAULT_FILE
    return filename


def apply_filter(image):
    for pixel in image:
        pixel.red = pixel.red * 1.5
        pixel.green = pixel.green * 0.7
        pixel.blue = pixel.blue * 1.5
    return image


if __name__ == '__main__':
    main()