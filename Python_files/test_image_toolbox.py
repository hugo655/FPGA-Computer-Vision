import image_toolbox as it
import numpy as np
import unittest
import cv2 as cv

class Test_image_toolbox(unittest.TestCase):
    def test_sanity(self):
        my_array = np.ones((3,4))
        ref_array = np.ones((3,4))
        np.testing.assert_array_equal(my_array, ref_array)

    def test_corr(self):
        demo_img = it.impulse_5x5()
        w = it.kernel_generator(0)
        output_corr = it.corr(demo_img,w)
        output_cv = cv.filter2D(src=demo_img, ddepth=-1, kernel=w)
        np.testing.assert_array_equal(output_cv, output_corr)


if __name__=='__main__':
	unittest.main()
    
    

    