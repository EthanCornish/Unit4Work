''' This program takes a directory from the user and opens the image file in preview.'''

from PIL import Image, ImageFilter  # imports the image library

imageFile = input('Enter the directory of the image you wish to show.')

try:
    image = Image.open(imageFile) # load an image from the hard drive
    image.show()  # displays the image
except FileNotFoundError:
    print('The file was not found')