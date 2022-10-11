# Prediction Algorithms

## Introduction

30 models are built for the project. 26 models are utilized to predict crop yield in across the Australia and each state
in Australia. 4 models are used to predict crop export price

### Crop

|Wheat| Oat | Corn | Barley |
|:---:|:---:|:----:|:------:|

### Input for crop yield prediction models

Monthly data: Humidity, Wind, Ultraviolet A, Ultraviolet B, Temperature, Rainfall, Evaporation

Single value data: Plating area, Fertilizer, Covid19 (binary value)

### Input for export price prediction models

Data in each continent(America, Asia, Europe,Oceania): Crop Production, Export volume, Trade value

Single value data: Oil price, Covid19

## Dataset Preprocessing

The dataset will be divided into five folders. Cross-Validation will be applied during the process of training.
Considering we only have limited data, we will not split test set from the whole dataset. After using Cross-Validation,
we can get the best hyperparameters for each model and then use the whole dataset to retrain the model. As for the
preprocessing, we normalize the whole dataset into range [0,1] to avoid numerical instability during the process of
training.

## Machine Learning Algorithms

The algorithms used to predict crop yields are all machine learning algorithms including ElasticNet, Support Vector
Machine, KNeighborsRegressor, GaussianProcessRegressor, DecisionTree and DeepNeuralNetwork. We will mainly evaluate the
model from two aspects: performance and efficiency. We will use average margin of error as the measurement of
performance. As for efficiency, calculation speed will be taken into consideration.

### ElasticNet

ElasticNet a linear regression model trained with both l1 and l2 -norm regularization of the coefficients. Elastic-net
is useful when there are multiple features that are correlated with one another.

### Support Vector Machine

Support Vector Machine is normally used in classification, but it can be extented to solve regression problems. The
model produced by Support Vector Regression depends only on a subset of the training data, because the cost function
ignores samples whose prediction is close to their target.

### KNeighborsRegressor

Neighbors-based regression can be used in cases where the data labels are continuous rather than discrete variables. The
label assigned to a query point is computed based on the mean of the labels of its nearest neighbors.

### GaussianProcessRegressor

The GaussianProcessRegressor implements Gaussian processes (GP) for regression purposes. For this, the prior of the GP
needs to be specified. The prior mean is assumed to be constant and zero or the training data’s mean. The prior’s
covariance is specified by passing a kernel function

### Decision Tree

Decision Trees (DTs) are a non-parametric supervised learning method used for classification and regression. The goal is
to create a model that predicts the value of a target variable by learning simple decision rules inferred from the data
features. A tree can be seen as a piecewise constant approximation.

### Deep Neural Network

Multi-layer Perceptron (MLP) is a supervised learning algorithm that learns a function by training on a dataset. Given a
set of features and a target , it can learn a non-linear function approximator for either classification or regression.

### Convolutional Neural Network

CNN is normally uesd in Computer Vision to extract features from a 2D image. We reshape out 1D input vector into 2D
matrix and use CNN to extract features.

### Recurrent Neural Network

RNN is normally used in Natural Language Processing. The input of a RNN is normally a sentence with many words. Each
word is a vecter with the same length. We split out input data in this way and feed it to a RNN.

## Model Comparison

We use the wheat yield prediction across Australia task to build and compare different models. Average margin of error(
training error)
is used to measure the performance of models.

|          Model Name          |                    Model Parameters                     | Average Margin of Error |             Evaluation             |
|:----------------------------:|:-------------------------------------------------------:|:-----------------------:|:----------------------------------:|
|          ElasticNet          |               alpha: 0.025 l1_ratio: 1.0                |          19.4%          |       Simple,Fast,Inaccurate       |
|    Support Vector Machine    |                         C: 0.7                          |          11.9%          |       Simple, Fast, Accurate       |
|     KNeighborsRegressor      |                 Number of neighbors: 7                  |          25.3%          | No need to train, Slow, Inaccurate |
|   GaussianProcessRegressor   |                Prior:0 Kernel:DotProduct                |          13.2%          |      Complex, Fast, Accurate       |
|        Decision Tree         | max_depth: 10 min_samples_split: 8  min_samples_leaf: 2 |          12.8%          |       Simple, Fast, Accurate       |
|     Deep Neural Network      |              please review the source code              |          8.3%           |      Complex, Fast, Accurate       |
| Convolutional Neural Network |              please review the source code              |          15.8%          |      Complex, Fast, Accurate       |
|   Recurrent Neural Network   |              please review the source code              |          12.6%          |      Complex, Fast, Accurate       |

## Model Performance

We use DNN as our final prediction models.

### Prediction models for Australia

|           Model Name           | Average Margin of Error |
|:------------------------------:|:-----------------------:|
|     Wheat Yield Prediction     |          6.74%          |
|    Barley Yield Prediction     |          8.63%          |
|      Oat Yield Prediction      |          7.23%          |
|     Corn Yield Prediction      |          3.61%          |
| Wheat Export Price Prediction  |          4.73%          |
| Barley Export Price Prediction |          4.89%          |
|  Oat Export Price Prediction   |          6.86%          |
|  Corn Export Price Prediction  |         12.49%          |

### Prediction models for NSW

|           Model Name           | Average Margin of Error |
|:------------------------------:|:-----------------------:|
|     Wheat Yield Prediction     |         11.81%          |
|    Barley Yield Prediction     |         13.22%          |
|      Oat Yield Prediction      |         10.88%          |
|     Corn Yield Prediction      |          6.08%          |

### Prediction models for QLD

|           Model Name           | Average Margin of Error |
|:------------------------------:|:-----------------------:|
|     Wheat Yield Prediction     |          6.26%          |
|    Barley Yield Prediction     |         10.33%          |
|      Oat Yield Prediction      |         13.20%          |
|     Corn Yield Prediction      |          8.72%          |

### Prediction models for SA

|           Model Name           | Average Margin of Error |
|:------------------------------:|:-----------------------:|
|     Wheat Yield Prediction     |         10.25%          |
|    Barley Yield Prediction     |          8.72%          |
|      Oat Yield Prediction      |          7.83%          |

### Prediction models for TA

|           Model Name           | Average Margin of Error |
|:------------------------------:|:-----------------------:|
|     Wheat Yield Prediction     |         12.71%          |
|    Barley Yield Prediction     |          8.88%          |
|      Oat Yield Prediction      |         10.45%          |

### Prediction models for Vic

|           Model Name           | Average Margin of Error |
|:------------------------------:|:-----------------------:|
|     Wheat Yield Prediction     |         12.87%          |
|    Barley Yield Prediction     |         13.63%          |
|      Oat Yield Prediction      |          8.94%          |
|     Corn Yield Prediction      |         15.26%          |

### Prediction models for Wa

|           Model Name           | Average Margin of Error |
|:------------------------------:|:-----------------------:|
|     Wheat Yield Prediction     |          8.15%          |
|    Barley Yield Prediction     |         12.84%          |
|      Oat Yield Prediction      |          4.18%          |
|     Corn Yield Prediction      |          9.08%          |

### Failure Case

We plan to predict crop local price in each state. But we found that the data we have collected are not suitable for
local price prediction.

### Further improvement

We think that the overall performance of our prediction models is descent. But we still give some directions that can
further improve the models.

1. Collect more data, more data means more possibility.

2. Fully adjust the architecture and fine-tune a CNN or RNN.

3. Apply double machine learning during the process of data preprocessing

