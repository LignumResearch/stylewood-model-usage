# StyleWood: Training and using GANs to generate microscopic cross-section images of hardwood species

These species don't exist. StyleGAN generated microscopic cross-section images of hardwood species. 
<img src="https://github.com/LignumResearch/stylewood-model-usage/blob/main/images/mosaic.png?raw=true" alt="Mosaic of randomly generated images using our model." width="830"/>


This repository was created to provide the original implementation for the paper under review  "**Creating high-resolution microscopic cross-section images of hardwood species using generative adversarial networks**" 



In this repository, you will find the code used for training and using the model. Here is a basic summary of the directories found in this repository:

- **collab/**: Contains notebook, generator and code for web application. [See and use the notebook on Collab](https://colab.research.google.com/drive/1U0NU7CLlW3gTYVzwlYEgANfd8Uh7vFkc?usp=sharing) .
- **dnnlib/**: StyleGAN related.
- **images/**: Images produced for this repository (used in Readme).
- **metrics/**: Contains FID score calculation
- **results/**: Contains model's trained snapshot at 7446 kimg selected to show implementation.
- **training/**: StyleGAN related. Adjusted to use cross-sectional images of hardwoods species.

## System requirements

* CentOS Linux 7. **Not tested in Windows.
* 64-bit Python 3.7 installation.
* TensorFlow 1.14 with GPU support.
* One or more high-end NVIDIA GPUs with at least 11GB of DRAM. We recommend NVIDIA RTX 2080 Ti GPU.
* NVIDIA driver 411.63, CUDA toolkit 10.0, cuDNN 7.6.4.

## How to use?
__[step 1.] Prepare dataset__ 

* Make sure to download the TFRecords of the dataset [here](https://drive.google.com/file/d/1uYK-whQluEXNoqvnAp-Se9tdxi_4XNfj/view?usp=sharing)

__[step 2.] Config__:

1. Edit [train.py](./train.py) with the path of the unzipped file from step 1. Change **Line 37
2. Edit [train.py](./train.py) lines 40-43 with the number of GPUS that will be used for training. By default, 4 GPUS will be used. 

__[step 3.] Training__:

1. Run [train.py](./train.py) as ```python train.py```. 

* **Bear in mind that StyleGAN is extremely computational expensive.
* Visualization of training progress can be done by TensorBoard. 
* Within the results folder, a new directory will be created with training information.
* Training is expected to last days (maybe weeks) depending on computational power. 

__[step 4.] Image generation__:

1a. You can use [random_figure.py](./random_figure.py) to generate 100 images using the author's snapshot. If you want to generate a different number of images, change line 33 in the same file. 

1b. You can also use your own snapshot generated by your training stage. If that is the case, change line 26 with your own snapshot in [random_figure.py](./random_figure.py). 

## Don't want to train it, but want to use it?

See our google Collab [here](https://colab.research.google.com/drive/1U0NU7CLlW3gTYVzwlYEgANfd8Uh7vFkc?usp=sharing). In the collab you will be to generate image transitions as the below. 

<img src="https://github.com/LignumResearch/stylewood-model-usage/blob/main/images/transition.gif?raw=true" alt="Transition using our generator." width="512">


## Credits and Rerences
For the paper, we trained StyleGAN to generate synthetic images and used XDD microscopic cross sections of hardwood species dataset. 

- A Style-Based Generator Architecture for Generative Adversarial Networks. Tero Karras (NVIDIA), Samuli Laine (NVIDIA), Timo Aila (NVIDIA). [https://arxiv.org/abs/1812.04948](https://arxiv.org/abs/1812.04948). [StyleGAN — Official TensorFlow Implementation](https://github.com/NVlabs/stylegan).

To train StyleGAN, we used a dataset containing identified microscopic cross-sectional images of hardwoods species by the XDD research team.

- SUGIYAMA, Junji, HWANG, Sung Wook, ZHAI, ShengCheng, KOBAYASHI, Kayoko, KANAI, Izumi, KANAI, Keiko. [Xylarium Digital Database for Wood Information Science and Education](http://hdl.handle.net/2433/250016).

The complete set of references can be found in our paper. 
