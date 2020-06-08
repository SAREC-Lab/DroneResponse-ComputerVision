# Week 1 Tasks 
1. Complete CRC Tutorial 
2. Dataset Preparation 
3. Training Classifier 

The main focus of this week is getting familiar with CRC resources and getting the data sets prepared. If all this gets completed, then we can start with training classifiers! Otherwise no worries, we will get to that piece soon! :) 

## (Part 2) Dataset Preparation 

### General Overview of Vision Task 

We are going to create multiple independent binary classifiers for each condition we will want to query in the **Weather Station**. For example, maybe we want to know whether it is foggy in the current frame of interest. It is binary because we just want a 'yes' or 'no'. 

To give you all an experience in finding and considering aspects and details about data, I have planned out the weather component and will challenge you guys to consider and develop a plan for the daylight conditions. 

#### Weather 

Here are some weather conditions to consider: 

- Sunny 
- Cloudy 
- Foggy 
- Rainy 
- Snowy 

We will thus want to create 5 binary classifiers which will handle these weather conditions. Each of the classifiers will be able to determine whether the weather condition is present or not. 

Here is a publically available dataset that can be utilized for this: 
[Weather Data](https://www.cs.ccu.edu.tw/~wtchu/projects/Weather/index.html) 

#### Daylight conditions

> What are some good conditions to consider for daylight conditions?

> What are some potentially available datasets we can use to accomplish this?

### Organizing the Data 

**DATA IS SO IMPORTANT**

<p align="center">
  <img src="https://uploads-ssl.webflow.com/5e21ab5d4dccf7f3cbe6bf39/5e3bdc5f2dd2113741d44618_1-Understand.gif" width="300" height="300"/>
</p>

Preparing the data will probably be one of the more time consuming aspects of this process. I know it probably isnt the most fun or exiciting thing, but it is **IMPORTANT** you take delicate care in forming these datasets, otherwise you will face many difficulties trying to train these classifiers. 

To place it more into perspective imagine if someone showed you a dog and cat, but told you that both examples were that of 'dog'. You would probably have a pretty hard time deciphering what was what. 

<p align="center">
  <img src="https://cdn.dribbble.com/users/6191/screenshots/3618049/teddy_food_dribbble.gif" width="500" height="500"/>
</p>

The same will happen with the model. If while prepping the data you mix up the images and the classes are incorrect, the model will have a hard time learning the correct underlying patterns and will fail when applied to a task. 

Here is the general structure the folders should take. 

```bash
|--|--dataset (folder)
|--|--|--train (folder)
|--|--|--|--class (folder)
|--|--|--|--|--image_1
|--|--|--|--|--image_2
|--|--|--|--|--...
|--|--|--|--not_class (folder)
|--|--|--|--|--image_1
|--|--|--|--|--image_2
|--|--|--|--|--...
|--|--|--test (folder)
|--|--|--|--image_1
|--|--|--|--image_2
```
For example, for the sunny class, the data will be organized as follows: 

```bash
|--|--dataset (folder)
|--|--|--train (folder)
|--|--|--|--sunny (folder)
|--|--|--|--|--image_1
|--|--|--|--|--image_2
|--|--|--|--|--...
|--|--|--|--not_sunny (folder)
|--|--|--|--|--image_1
|--|--|--|--|--image_2
|--|--|--|--|--...
|--|--|--test (folder)
|--|--|--|--image_1
|--|--|--|--image_2
```

- There should be a separate dataset for each condition. For the weather example you will need 5: one for `sunny`, `cloudy`, `foggy`, `rain`, and `snow`. 
- The dataset will contain two folder `train` and `test`. 
- `train` will be the images which are used to train (surprise!) the model. This folder will contain two subfolders, the `class` and the `not_class `. 
- Using the example for `sunny`, in `class`, this folder will contain images that are representative of sunny instances and should only contain examples of sunny images. `not_class` will contain examples that are not representative of sunny, which will be a mix of foggy, snowy, rainy and cloudy. 
- `test` should contain a mix of image that are **NOT** in `train`. These will be the images that are used to evaluate how well the model works on untrained data, so you need to make sure that these are unique images no where in the train folder!! We want to make sure the model can make the correct prediction without having seen the image and its label before. 

Another important thing to consider is the number of images in each folder. The weather dataset I have linked is broken up in the following manner: 

| Class  | # Of Images |
| ------------- | ------------- |
| Sunny  | 70,501 |
| Cloudy  | 45,662  |
| Snowy  | 1,252  |
| Rainy  | 1,369  |
| Foggy  | 357  |
| Other | 64,657 |

As we can see, the distribution is not equal among the images. However, we want our `class` and `not_class` folder to have approximately the same number of images. For example for the `sunny` case, the `sunny` folder would contain 1428 images from Sunny and then 357 images from each other other classes in the `not_sunny` folder so this folder too would have 1428 images. 

It is also important to note that the more data available, the better it is. So if there are images from other datasets that can be added to this to increase the number of examples for the less represented classes, then it would be incredibly helpful when training to have that included! 

Considering the number of images in `test` is just a matter of having a good representation to evaluate how well the model is working. Get a handful of images from each of the classes and also generate a `.csv` file that contains the correct label for each image in `test` which can be used to make sure the model classified the images correctly. 

I would ignore the `Other` class of images. These are the images with unclear weather conditions. 

Since these images will also be deployed on drones, we want to see how well these classifiers will perform on examples of images captured from drones. The datasets collected from the UG^2 challenge is perfect for this: http://cvpr2020.ug2challenge.org/

However, the data collected from these challenges are in the form of videos, so the frames will need to be extracted and placed in the correct folders. 

The data prep part is usually the least fun for peeps, but once it is over the fun part of computer vision approaches! :) Just make sure to take care in preparing it because creating the classifiers will eitherwise become a nightmare! It is worth taking the time to do well! 
