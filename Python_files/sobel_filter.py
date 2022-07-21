#!/bin/python

import sys
import os
import imageio as iio
import matplotlib.pyplot as plt

# Import image
image_path = sys.argv[1]
image = iio.imread(image_path)

print(image.shape)
plt.imshow(image)
plt.show()