
#   [x] display grey image function  
#   [ ] image_convolution function

import matplotlib.pyplot as plt
import numpy as np


def show_img_grey(grey_img: np.ndarray):
    plt.imshow(demo_img,cmap='gray',vmin=0,vmax=255)
    plt.show()


demo_img = np.zeros((9,9))

demo_img[:5,:] = 200
demo_img[5:,:] = 120

show_img_grey(demo_img)

