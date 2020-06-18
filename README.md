# Using Conda to Create Virtual Environments

## Installing Anaconda 
Install Anaconda to your computer using this link: https://www.anaconda.com/products/individual. Since this includes many packages that you may not need, if you would prefer to install only the things you need, you can install condo using this link: https://docs.conda.io/en/latest/miniconda.html

## Creating and Activating Virtual Environments
You can create a virtual environment via Anaconda navigator or command line. If you use Anaconda Navigator, simply go to the “Environments” tab on the left, and select “Create” to make a new environment. Name your environment and choose your packages accordingly. 

## Using Command Line 
If you would like to create and activate a virtual environment through command line, first check that your conda is up to date using: 
`conda update conda`
To create a new conda environment, use:
`conda create -n yourenvname python=x.x anaconda` where x.x is the Python version you would like to use. 
To activate the conda environment, use:
`source activate yourenvname`
If you would like to see the list of your environments, you can use:
`conda info -e`
To install more packages to your environment, you can use:
`conda install -n yourenvname [package]`
Finally, to end a session in the current environment, use:
`source deactivate`. Finally, if you would like reactivate your environment, simply type: `conda activate yourenvname`