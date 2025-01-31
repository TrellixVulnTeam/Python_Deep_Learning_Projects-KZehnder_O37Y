# Kevin Zehnder : Project Home
<p align="center">
  <img src="docs/jpegs/readme/job1_resized.jpg">
</p>

Looking for a ***job!*** Please contact me at ***kjzehnder3@gmail.com*** if you are hiring and believe I could add value to your business!

## Dash SP500 Stocks ([click to view project code](Dash_Plotly_SP500/))
<p align="center">
  <img src="docs/jpegs/dash_sp500/dash_sp500.gif">
</p>

## 7. Faster R-CNN Hand Sanitizer Clorox Wipes Detector ([click to view project code](Hand_Sanitizer_Detector/))

***Note***: Images and annotation files are included in this repository if you want to use them and train your own model ([click to view images and XML annotation files](Hand_Sanitizer_Detector/images))

 Sample prediction #1      |  Sample prediction #2
:-------------------------:|:-------------------------:
![alt-text-1](docs/jpegs/7_sanitizer/usage2.png "title-1") | ![alt-text-2](docs/jpegs/7_sanitizer/usage1.png "title-2")

 Sample prediction #3      |  Sample prediction #4 
:-------------------------:|:-------------------------:
![alt-text-1](docs/jpegs/7_sanitizer/usage3.png "title-1") | ![alt-text-2](docs/jpegs/7_sanitizer/usage4.png "title-2")

Use this EXCELLENT tutorial series if you want to learn how to build your own custom object detectors using Tensorflow Object Detection API: https://pythonprogramming.net/introduction-use-tensorflow-object-detection-api-tutorial/

If you are interested in using code directly from this repository please keep in mind that certain files in the "models" folder are too large to upload onto github. Secondly, the Tensorflow Object Detection API only works for me when I use ***tensorflow==1.13.2*** (pip install --upgrade tensorflow==1.13.2) and the ***models version*** that can be found here: https://github.com/tensorflow/models/archive/v1.13.0.zip 

If you want to view a standalone version of the Hand Sanitizer Clorox Wipes Detector I have created a seperate repository to do so here: https://github.com/righttrianglesrkewl3/Hand_Sanitizer_Clorox_Wipe_Detector

## 1. Hockey Faster R-CNN Tensorflow Object Detection API Example ([click to view project code](Faster_R-CNN_Tensorflow_Object_Detector/))

Use this ***EXCELLENT*** tutorial series if you want to learn how to build your own custom object detectors using Tensorflow Object Detection API: https://pythonprogramming.net/introduction-use-tensorflow-object-detection-api-tutorial/

Sample prediction #1      |  Sample prediction #2
:-------------------------:|:-------------------------:
![alt-text-1](docs/jpegs/1_tensor/resized_ten1.png "title-1") | ![alt-text-2](docs/jpegs/1_tensor/resized_ten2.png "title-2")

 Sample prediction #3      |  Tensorboard 
:-------------------------:|:-------------------------:
![alt-text-1](docs/jpegs/1_tensor/resized_individualImage.png "title-1") | ![alt-text-2](docs/jpegs/1_tensor/resized_board_training.png "title-2")

## 2. Facial Recognition ([Click here to view project code](Presidential_Candidate_Detector/))

<p align="center">
  <img src="docs/jpegs/2_president/candidates_facial_recognition.jpg">
</p>

## 3. Fruit VGG-16 classifier ([click here to view project code](Fruit_VGG_Feature_Extractor_Logistic_Classifier/))

Fruit Example #1 (class=Banana)                |  Fruit Example #2 (class=Apple)
:-------------------------:|:-------------------------:
![alt-text-1](docs/jpegs/3_fruit_VGG/peg2.png "title-1") | ![alt-text-2](docs/jpegs/3_fruit_VGG/peg1.png "title-2")

Fruit Model Metrics              |  Fruit Rank-1/Rank-5 Accuracy
:-------------------------:|:-------------------------:
![alt-text-1](docs/jpegs/3_fruit_VGG/metrics_fruit_train_feat_extract_logistic.png "title-1") | ![alt-text-2](docs/jpegs/3_fruit_VGG/fruit_rank_5.png "title-2")

## 4. Soda Bottles Transfer Learning -- miniVGG16net([click here to view project code](Sodas_miniVGGnet_Augmentation/))

Soda Bottle Example #1 (class=P.Cherry)            |  Soda Bottle Example #2 (class=MD.Diet)
:-------------------------:|:-------------------------:
![alt-text-1](docs/jpegs/4_soda_miniVGG/1278.jpg "model-metrics") | ![alt-text-2](docs/jpegs/4_soda_miniVGG/1672.jpg "title-2")

Soda Bottle Model Metrics ***with*** Augmentation            |  Soda Bottle Training Plot ***with*** Augmentation
:-------------------------:|:-------------------------:
![alt-text-1](docs/jpegs/4_soda_miniVGG/metrics_soda_augmented.png "model-metrics") | ![alt-text-2](docs/jpegs/4_soda_miniVGG/vgg16net_augmentation_soda_training_plot.png "training-plot")

Soda Bottle Model Metrics ***without*** Augmentation            |  Soda Bottle Training Plot ***without*** Augmentation
:-------------------------:|:-------------------------:
![alt-text-1](docs/jpegs/4_soda_miniVGG/metrics_soda_vgg16net_no_augmentation_notebook_classification_report.png "model-metrics") | ![alt-text-2](docs/jpegs/4_soda_miniVGG/soda_vgg16net_no_augmentation_training_plot.png "title-2")

## 5. Boats Transfer Learning -- ResNet50 ([click here to view project code](Boats_ResNet50/))

Model Metrics              
:-------------------------:|
![alt-text-1](docs/jpegs/5_Boats_ResNet50_Transfer_Learning/metrics_boats_kaggle.png "model-metrics") 


# Citations
Code in this repository is heavily adapted from course content in **PyImageSearch Gurus** and **Deep Learning for Computer Vision with Python** by **Dr. Adrian Rosebrock**. Please visit **https://www.pyimagesearch.com/pyimagesearch-gurus/** for additional information.
<p align="left">
  <img src="docs/jpegs/citation.png">
</p>
