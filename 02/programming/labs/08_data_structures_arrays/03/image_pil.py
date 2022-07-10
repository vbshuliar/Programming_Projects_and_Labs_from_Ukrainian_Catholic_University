import numpy as np

# Importing Image and ImageOps module from PIL package
from PIL import Image, ImageOps

# creating a image object
image = Image.open(r"a37-286x300.jpg")

# creating greyscale image object by applying greyscale method
image_grayscale = ImageOps.grayscale(image)

# size of image
print(image_grayscale.size)

# image as numpy array of pixel
img_array = np.array(image_grayscale)
print(img_array.shape)
print(img_array[299, 285])

# pixels of image as PixelAccess object
pixels = image_grayscale.load()
print(pixels[34, 34])
pixels[34, 34] = 0
print(pixels[34, 34])

for i in range(286):
    for j in range(300):
        print(pixels[i, j])

# using getpixel method for pixel access
cordinate = x, y = 150, 59
print(image_grayscale.getpixel(cordinate))

# show image
image_grayscale.show()

# change and save image
img_array = img_array - 100
new_img = Image.fromarray(img_array)

new_img.show()
