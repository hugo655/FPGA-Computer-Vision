#!/bin/python


import sys
import os
import imageio as iio
import matplotlib.pyplot as plt
import numpy as np
import image_toolbox as it

image_path = sys.argv[1]
img_rgb =np.array(iio.imread(image_path))
img = it.rgb2grey(img_rgb)

G,Gy,Gx = it.sobel(img)

it.show_img_grey(G)


