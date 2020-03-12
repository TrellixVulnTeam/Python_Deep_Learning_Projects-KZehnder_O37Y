# Kevin Zehnder : Selected Projects

## 1. Tensorflow Object Detection API Example ([click to view project code](1_faster_rcnn_tensorflow/))

 Sample prediction #1      |  Sample prediction #2
:-------------------------:|:-------------------------:
![alt-text-1](docs/jpegs/1_tensor/resized_ten1.png "title-1") | ![alt-text-2](docs/jpegs/1_tensor/resized_ten2.png "title-2")


## 2. President Detector ([Click here to view project code](2_president_detector/))

<p align="center">
  <img src="docs/jpegs/2_president/candidates_facial_recognition.jpg">
</p>

## 3. Fruit VGG-16 classifier ([click here to view project code](3_fruit_VGG_feature_extractor_logistic/))

features extracted from final pool layer of VGG conv net and a logisitic regression classifier was trained on top

Model Metrics              |  Rank-1/Rank-5 Accuracy
:-------------------------:|:-------------------------:
![alt-text-1](docs/jpegs/3_fruit_VGG/metrics_fruit_train_feat_extract_logistic.png "title-1") | ![alt-text-2](docs/jpegs/3_fruit_VGG/fruit_rank_5.png "title-2")

model=miniVGG16 dropout=False augmentation=False

## 4. Soda Bottles Transfer Learning -- miniVGG Feature Extractor + Logistic ([click here to view project code](4_soda_bottles_minivggnet_classifier/))

features extracted from final pool layer of miniVGG conv net and a logisitic regression classifier was trained on top

Model Metrics            |  Sample prediction #1
:-------------------------:|:-------------------------:
![alt-text-1](doc/jpegs/metrics_width_580.jpg "model-metrics") | ![alt-text-2](doc/jpegs/metrics_width_400.jpg "title-2")

## 5. Boats Transfer Learning -- Fine-Tuning ([click here to view project code](5_transfer_learning_fine_tuning/))

features extracted from final pool layer of miniVGG conv net and a logisitic regression classifier was trained on top

Model Metrics            |  Sample prediction #1
:-------------------------:|:-------------------------:
![alt-text-1](doc/jpegs/metrics_width_580.jpg "model-metrics") | ![alt-text-2](doc/jpegs/metrics_width_400.jpg "title-2")



# Citations
Code in this repository is heavily adapted from course content in the **PyImageSearch Gurus** and **Deep Learning for Computer Vision with Python** by Dr. Adrian Rosebrock. Please visit **https://www.pyimagesearch.com/pyimagesearch-gurus/** for additional information.
<p align="left">
  <img src="docs/jpegs/citation.png">
</p>
