"""
This program creates a 22x22 pixel images.
"""
# Installs:
# python -m pip install PIllow

# Imports:
# first include simpleimage.py in the project folder
from simpleimage import SimpleImage

# Constants:


def main():
    image = SimpleImage.blank(22, 22)

    width = image.width
    height = image.height

    image = make_frame(width, height, image)
    image.show()


def make_star(width, height, image):
    # for the lines:
    pixel =


def make_frame(width, height, image):
    for x in range(width):
        for y in range(height):
            if x <= 0 or x >= 21 or y <= 0 or y >= 21:
                pixel = image.get_pixel(x, y)
                new_pixel = pixel
                new_pixel.red = 0
                new_pixel.green = 0
                new_pixel.blue = 0
                image.set_pixel(x, y, new_pixel)
    return image


def turn_black(width, height, image):
    for x in range(width):
        for y in range(height):
            pixel = image.get_pixel(x, y)
            new_pixel = pixel
            new_pixel.red = 0
            new_pixel.green = 0
            new_pixel.blue = 0
            image.set_pixel(x, y, new_pixel)
    return image


if __name__ == '__main__':
    main()