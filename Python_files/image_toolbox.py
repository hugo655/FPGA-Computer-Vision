
#   [x] display grey image function  
#   [ ] image_convolution function


from matplotlib import image
import matplotlib.pyplot as plt
import numpy as np


def rgb2grey(rgb_img: np.ndarray):
    grey_img = 0.299*rgb_img[:,:,0] + 0.587*rgb_img[:,:,1] + 0.114*rgb_img[:,:,2]    
    return grey_img

def show_img_grey(grey_img: np.ndarray):
    plt.imshow(grey_img,cmap='gray',vmin=0,vmax=255)
    plt.show()

def pad_image(img: np.ndarray, kernel_size: int):
    kernel_border_size = kernel_size-1
    k = int(kernel_border_size/2)
    y_dim,x_dim = np.shape(img)
    x_pad = int(x_dim+kernel_border_size)
    y_pad = int(y_dim+kernel_border_size)
    padded_image = np.zeros((y_pad,x_pad))
    for y in range(y_dim):
        for x in range(x_dim):
            padded_image[k+y,k+x] = img[y,x]
    return padded_image

def corr(img, kernel):
    padded_image = pad_image(img,kernel.shape[0])
    output_image = slide_and_multiply(padded_image,kernel)
    return output_image

def cov(img, kernel):
    padded_image = pad_image(img,kernel.shape[0])
    fliped_kernel = kernel[::-1,::-1]
    output_image = slide_and_multiply(padded_image,fliped_kernel)
    return output_image

def slide_and_multiply(img: np.ndarray, kernel: np.ndarray):
    #Defining Variables to limit the border
    y_dim, x_dim = np.shape(img)
    kernel_frame_size = kernel.shape[0]-1
    k = int(kernel_frame_size/2)
    
    output_img_x_dim = int(x_dim-kernel_frame_size)
    output_img_y_dim = int(y_dim-kernel_frame_size)
    output_img = np.zeros((output_img_y_dim,output_img_x_dim))

    y_max_range = int(y_dim-k)
    x_max_range = int(x_dim-k)
    for y in range(k,y_max_range):
        for x in range(k,x_max_range):
            sample = img[y-k:y+k+1,x-k:x+k+1]
            output_img[y-k,x-k] = np.sum(np.multiply(sample,kernel))
    
    return output_img

def sobel_coeficients():
    Gx = np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
    Gy = np.array([[1,2,1],[0,0,0],[-1,-2,-1]])
    return Gy,Gx

def kernel_generator(type=0):
    if(type == 0):
        kernel = np.array([[1,2,3],[4,5,6],[7,8,9]])  
    elif(type == 1):
        kernel = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])  
    return kernel

def impulse_5x5():
    unit_impulse = np.zeros((5,5))
    unit_impulse[2,2] = 1
    return unit_impulse

