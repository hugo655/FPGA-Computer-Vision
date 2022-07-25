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
        demo_img = it.gradient_generator(2,100)
        w = it.kernel_generator(0)
        output_corr = it.corr(demo_img,w)
        output_cv = cv.filter2D(src=demo_img, ddepth=-1, kernel=w)

        #Remove the border
        output_corr = np.delete(output_corr,[0,-1],0)
        output_corr = np.delete(output_corr,[0,-1],1)
        output_cv = np.delete(output_cv,[0,-1],0)
        output_cv = np.delete(output_cv,[0,-1],1)

        np.testing.assert_array_equal(output_cv, output_corr)
   
    def test_cov(self):
        demo_img = it.gradient_generator(2,100)
        w = it.kernel_generator(1)
        output_cov = it.cov(demo_img,w)
        output_cv = cv.filter2D(src=demo_img, ddepth=-1, kernel=w[::-1,::-1])

        #Remove the border
        output_cov = np.delete(output_cov,[0,-1],0)
        output_cov = np.delete(output_cov,[0,-1],1)
        output_cv = np.delete(output_cv,[0,-1],0)
        output_cv = np.delete(output_cv,[0,-1],1)

        np.testing.assert_array_equal(output_cv, output_cov)

if __name__=='__main__':
	unittest.main()
    
    

    