# Week 2

All done with the not so fun part! Onto training classifiers! 

I have included a jupyter notebook that has everything you will need to start practicing with training a vision classifier for **Apples** and **Not_Apples** which are just oranges.

Maybe you have never used a jupyter notebook before. That is okay! Here is a great reference: https://realpython.com/jupyter-notebook-introduction/ 

I recommend creating a conda virtual environment and running the jupyter notebook from there. By doing this you can make sure your libraries and specific versions are isolated. Errors related to a package can easily be solved, just run `conda install <package name>` after activating your environment. 

```sh 
# create your environment 
conda create --name DroneResponse python=3.7

# activate your environment 
conda activate DroneResponse 

# either clone or pull this repo 
# clone if you have not downloaded yet 
git clone https://github.com/SAREC-Lab/DroneResponse-ComputerVision.git

# pull for updates by navigating to the repo and then running 
git pull 
```
You will then want to download the fruit dataset I provided in the google drive into the `Week_2` folder where the notebook is. 

Once that is downloaded, you can have the option of accessing your virtual environment to run your notebook from: 
```sh 
# from the environment run: 
conda install -c anaconda ipykernel
python -m ipykernel install --user --name=DroneResponse
```
You can then change the kernel in the notebook itself. Open jupyter notebook by running 
```sh
jupyter notebook 
```
This should open a window in your web browser. Navigate to the file `Training and Testing Computer Vision Classifier .ipynb`. Then once opened, go to `Kernel > Change Kernel > DroneResponse` or whatever the name of your virtual environment is. The top right corner should display the name of this environment below `Logout`. Now you have access to all the libraries in your virtual environment! 

If you need to install libraries, do the following for the package in need by opening a terminal, making sure your environment is activated and running `conda install <package name>`. 

```sh 
# examples of installing packages 
conda install scikit-learn
conda install -c anaconda numpy
conda install mahotas
```
After reviewing the jupyter notebook tutorial, you are good to go. You can run the cells by pressing `Shift`+`Enter`. 

I have included tasks you can aim to complete for this at the bottom of the notebook. I suggest getting an overiew of the notebook in total before trying to run the cells. Go ahead and read through and get a good grasp of the process and then play with it! 

You are now going to be feature magicians! How awesome! Best of luck, here if you need anything :) 

<p align="center">
  <img src="https://cdn.dribbble.com/users/2838660/screenshots/6237017/magician_dribbble_2.gif" width="500" height="300"/>
</p>


P.S. Kind of wrote this README half asleep, so I totally understand if something makes no sense and am happy to clarify xD 

