#!/bin/python


import sys
import os
import imageio as iio
import matplotlib.pyplot as plt
import numpy as np
import image_toolbox as it

# Import image
image_path = sys.argv[1]
image = np.array(iio.imread(image_path))

#Convert to Grey Scale
grey_img = it.rgb2grey(image)

Gy,Gx = it.sobel_coeficients()

del_x_cor = it.corr(grey_img,Gx)
del_y_cor = it.corr(grey_img,Gy)

G_cor = np.sqrt(del_x_cor**2+del_y_cor**2)

del_x_cov = it.corr(grey_img,Gx)
del_y_cov = it.corr(grey_img,Gy)

G_cov = np.sqrt(del_x_cov**2+del_y_cov**2)

print(it.images_equal(G_cov,grey_img))

