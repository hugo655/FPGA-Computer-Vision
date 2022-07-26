#!/bin/python

import sys
import numpy as np
import imageio as iio
import image_toolbox as it

image_path = sys.argv[1]
img_rgb =np.array(iio.imread(image_path))
img = it.rgb2grey(img_rgb)

G,Gy,Gx = it.sobel(img)

# Normalize the values 
G = G*1/8

# Invert the colors for better visualization
G = 255 - G

it.show_img_grey(G)
