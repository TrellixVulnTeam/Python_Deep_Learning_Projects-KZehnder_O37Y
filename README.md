# Kevin Zehnder : Selected Projects
***Note: Please see citations section at the bottom of this page***

## ***Urgent:*** Seeking a position as a software engineer in the Deep Learning/Computer Vision field (Python). 

## Please contact me at kjzehnder3@gmail.com for additional information if you are impressed by this project and feel that I could add value to your company. Thanks in advance.

## 7. Faster R-CNN Hand Sanitizer Clorox Wipes Detector ([click to view project code](7_SANITIZER/))

***Note***: Images and annotation files are included in this repository if you want to use them and train your own model ([click to view images and XML annotation files](7_SANITIZER/images))

 Sample prediction #1      |  Sample prediction #2
:-------------------------:|:-------------------------:
![alt-text-1](docs/jpegs/7_sanitizer/usage2.png "title-1") | ![alt-text-2](docs/jpegs/7_sanitizer/usage1.png "title-2")

 Sample prediction #3      |  Sample prediction #4 
:-------------------------:|:-------------------------:
![alt-text-1](docs/jpegs/7_sanitizer/usage3.png "title-1") | ![alt-text-2](docs/jpegs/7_sanitizer/usage4.png "title-2")

Use this EXCELLENT tutorial series if you want to learn how to build your own custom object detectors using Tensorflow Object Detection API: https://pythonprogramming.net/introduction-use-tensorflow-object-detection-api-tutorial/

If you are interested in using code directly from this repository please keep in mind that certain files in the "models" folder are too large to upload onto github. Secondly, the Tensorflow Object Detection API only works for me when I use ***tensorflow==1.13.2*** (pip install --upgrade tensorflow==1.13.2) and the ***models version*** that can be found here: https://github.com/tensorflow/models/archive/v1.13.0.zip 

If you want to view a standalone version of the Hand Sanitizer Clorox Wipes Detector I have created a seperate repository to do so here: https://github.com/righttrianglesrkewl3/Hand_Sanitizer_Clorox_Wipe_Detector

## 1. Hockey Faster R-CNN Tensorflow Object Detection API Example ([click to view project code](1_faster_rcnn_tensorflow/))

Use this ***EXCELLENT*** tutorial series if you want to learn how to build your own custom object detectors using Tensorflow Object Detection API: https://pythonprogramming.net/introduction-use-tensorflow-object-detection-api-tutorial/

Sample prediction #1      |  Sample prediction #2
:-------------------------:|:-------------------------:
![alt-text-1](docs/jpegs/1_tensor/resized_ten1.png "title-1") | ![alt-text-2](docs/jpegs/1_tensor/resized_ten2.png "title-2")

 Sample prediction #3      |  Tensorboard 
:-------------------------:|:-------------------------:
![alt-text-1](docs/jpegs/1_tensor/resized_individualImage.png "title-1") | ![alt-text-2](docs/jpegs/1_tensor/resized_board_training.png "title-2")

## 2. President Detector ([Click here to view project code](2_president_detector/))

<p align="center">
  <img src="docs/jpegs/2_president/candidates_facial_recognition.jpg">
</p>

## 3. Fruit VGG-16 classifier ([click here to view project code](3_fruit_VGG_feature_extractor_logistic/))

Fruit Model Metrics              |  Fruit Rank-1/Rank-5 Accuracy
:-------------------------:|:-------------------------:
![alt-text-1](docs/jpegs/3_fruit_VGG/metrics_fruit_train_feat_extract_logistic.png "title-1") | ![alt-text-2](docs/jpegs/3_fruit_VGG/fruit_rank_5.png "title-2")

Fruit Example #1 (class=Grape)                |  Fruit Example #2 (class=Apple)
:-------------------------:|:-------------------------:
![alt-text-1](docs/jpegs/3_fruit_VGG/0cf98cfa41c1ea17.jpg "title-1") | ![alt-text-2](docs/jpegs/3_fruit_VGG/0a8e8c51f6e6b723.jpg "title-2")

## 4. Soda Bottles Transfer Learning -- miniVGG16net([click here to view project code](4_sodas_miniVGGnet_augmentation/))

Soda Bottle Example #1 (class=P.Cherry)            |  Soda Bottle Example #2 (class=MD.Diet)
:-------------------------:|:-------------------------:
![alt-text-1](docs/jpegs/4_soda_miniVGG/1278.jpg "model-metrics") | ![alt-text-2](docs/jpegs/4_soda_miniVGG/1672.jpg "title-2")

Soda Bottle Model Metrics ***with*** Augmentation            |  Soda Bottle Training Plot ***with*** Augmentation
:-------------------------:|:-------------------------:
![alt-text-1](docs/jpegs/4_soda_miniVGG/metrics_soda_augmented.png "model-metrics") | ![alt-text-2](docs/jpegs/4_soda_miniVGG/vgg16net_augmentation_soda_training_plot.png "training-plot")

Soda Bottle Model Metrics ***without*** Augmentation            |  Soda Bottle Training Plot ***without*** Augmentation
:-------------------------:|:-------------------------:
![alt-text-1](docs/jpegs/4_soda_miniVGG/metrics_soda_vgg16net_no_augmentation_notebook_classification_report.png "model-metrics") | ![alt-text-2](docs/jpegs/4_soda_miniVGG/soda_vgg16net_no_augmentation_training_plot.png "title-2")

## 5. Boats Transfer Learning -- ResNet50 ([click here to view project code](5_boats_ResNet50/))

Model Metrics              
:-------------------------:|:-------------------------:
![alt-text-1](docs/jpegs/5_Boats_ResNet50_Transfer_Learning/metrics_boats_kaggle.png "model-metrics") 


# Citations
Code in this repository is heavily adapted from course content in **PyImageSearch Gurus** and **Deep Learning for Computer Vision with Python** by **Dr. Adrian Rosebrock**. Please visit **https://www.pyimagesearch.com/pyimagesearch-gurus/** for additional information.
<p align="left">
  <img src="docs/jpegs/citation.png">
</p>
