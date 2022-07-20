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
conda activate FPGA-Vision
conda list
```