#!/bin/python

from re import I
import sys
import os
import imageio as iio
import matplotlib.pyplot as plt
import numpy as np

def rgb2grey(rgb_img: np.ndarray):
    grey_img = 0.299*rgb_img[:,:,0] + 0.587*rgb_img[:,:,1] + 0.114*rgb_img[:,:,2]    
    return grey_img

# Import image
image_path = sys.argv[1]
image = np.array(iio.imread(image_path))

#Convert to Grey Scale
grey_img = rgb2grey(image)

y_dim, x_dim = grey_img.shape

print(x_dim, y_dim)

#Print image in grey scale
plt.imshow(grey_img,cmap='gray')
plt.show()


# print(image.shape)
# plt.imshow(image)
# plt.show()