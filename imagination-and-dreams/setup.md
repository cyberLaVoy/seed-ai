
## Python Libraries

```
pip install torch diffusers transformers accelerate
```

## Hardware and Drivers

1. Nvidia GPU with CUDA cores
2. Graphics driver
3. CUDA
4. cuDNN

The best way to obtain 2, 3, and 4 is to simply follow the instructions provided by Nvidia.

[Graphics driver](https://www.nvidia.com/download/index.aspx)

[CUDA](https://developer.nvidia.com/cuda-downloads)

[cuDNN](https://docs.nvidia.com/deeplearning/cudnn/install-guide/index.html)


To verify installs and check versions run:

```
nvidia-smi
```

--- 

Question:
> What is the difference between CUDA and cuDNN?

Answer:
> CUDA (Compute Unified Device Architecture) is a parallel computing platform and programming model developed by Nvidia for general-purpose computations on its graphics processing units (GPUs). It allows developers to use the power of the GPU to accelerate applications in fields such as scientific computing, machine learning, image and video processing, and more.
>
> cuDNN (CUDA Deep Neural Network library) is a GPU-accelerated library of primitives for deep neural networks. It provides highly tuned implementations of common deep learning operations such as convolution, pooling, and activation functions, which can greatly accelerate the training and inference of deep neural networks.
>
> CUDA is a broad platform that provides tools and libraries for a wide range of applications, while cuDNN is a specialized library focused specifically on accelerating deep learning applications. Both CUDA and cuDNN can be used together to build and run deep learning applications on Nvidia GPUs.

--- 

## Disabling Nouveau for Nvidia graphics driver install on Ubuntu server 

Create file:
```
sudo nano /etc/modprobe.d/blacklist-nouveau.conf
```

With the following contents:
```
blacklist nouveau
options nouveau modeset=0
```

Regenerate the kernel initramfs:
```
sudo update-initramfs -u
```

Finally, reboot.
```
sudo reboot
```


