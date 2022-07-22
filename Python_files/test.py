import matplotlib.pyplot as plt
import numpy as np


demo_img = np.zeros((9,9))

demo_img[0:5,:] = 255
demo_img[0:5,:] = 120


plt.imshow(demo_img,cmap='gray')
plt.show()
