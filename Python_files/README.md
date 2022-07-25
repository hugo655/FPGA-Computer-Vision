# Lane Detectection Algorithm

The first task is to implement the Sobel Filter algorithm for reading the 
sample files from `/sample_images`. 

```
1. Open Image
2. Loop for every pixel
    read pixels around pixels
    convert rgb to Y
    perform the sobel filter
    process the output (divide G/2 and subtract from 255)
```

To install any dependencies use anaconda as a package manager. The 
following commands are engough to setup the conda environment:

```
conda create --name FPGA-Vision
conda install -n FPGA-Vision scipy
conda install -n FPGA-Vision matplotlib
conda install -n FPGA-Vision imageio
conda install -c conda-forge opencv -n FPGA-Vision
conda activate FPGA-Vision
conda list
```

## About Image Processing in Python
There are a number of ways to read, write and process images using 
python. In these scripts, we are going to be using the module
[imageio](https://imageio.readthedocs.io/en/stable/index.html) 
for reading and writing operations.

Pyplot has a native method for displaying images, [imshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imshow.html)
we will use it for showing/ploting the results.

An alternativa to these modules is using [Open Cv](https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html)
Which can be installed using [conda-forge](https://anaconda.org/conda-forge/opencv).

