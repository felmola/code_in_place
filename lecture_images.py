"""
This is the Ancient Game of Nim. There is an initial pile of stones. Players take turns to take 1 or 2 stones from the
pile. The one that has the last turn before the stones runs out, wins the game.
"""
# Installs:
# python -m pip install PIllow

# Imports:
# first include simpleimage.py in the project folder
from simpleimage import SimpleImage

# Constants:


def main():
    image1 = SimpleImage("images/felix_the_cat.jpg")
    #image1.show()
    #SimpleImage.show(image1)

    #make_darker(image1)
    image1 = mirror(image1)
    3#image1.show()
    image1.show()


def mirror(image):
    image = image
    width = image.width
    height = image.height
    print(width)
    print(height)

    # Define a black image that is as hight as the original but twice as long.
    mirror = SimpleImage.blank(width * 2, height)

    # Create a nested for loop that assigns a pixel to the mirror image.
    for y in range(height):
        for x in range(width):
            pixel = image.get_pixel(x, y)
            mirror.set_pixel(x, y, pixel)
            mirror.set_pixel((width * 2) - (x + 1), y, pixel)

    return mirror


def make_darker(image):
    for pixel in image:
        pixel.red = pixel.red // 2
        pixel.green = pixel.greeb // 2
        pixel.blue = pixel.blue // 2


def make_brighter(image):
    for pixel in image:
        pixel.red = pixel.red * 2
        pixel.green = pixel.greeb * 2
        pixel.blue = pixel.blue * 2


if __name__ == '__main__':
    main()