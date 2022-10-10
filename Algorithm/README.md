# Prediction Algorithms

## Introduction

The algorithms used to predict crop yields are all machine learning algorithms including ElasticNet, Support Vector
Machine, KNeighborsRegressor, GaussianProcessRegressor, DecisionTree, DeepNeuralNetwork, ConvolutionalNeuralNetwork and RecurrentNeuralNetwork. We will mainly evaluate the
model from two aspects: performance and efficiency. We will use average margin of error as the measurement of
performance. As for efficiency, calculation speed will be taken into consideration.

## Dataset Preprocessing

The dataset will be divided into five folders. Cross-Validation will be applied during the process of training.
Considering we only have limited data, we will not split test set from the whole dataset. After using Cross-Validation,
we can get the best hyperparameters for each model and then use the whole dataset to retrain the model. As for the
preprocessing, we normalize the whole dataset into range [0,1] to avoid numerical instability during the process of
training.

## Machine Learning Algorithms

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

CNN is normally used in Computer Vision to extract features from 2D images. Reshape our input data to 
make it a 2D matrix and then use CNN to extract features.

### Recurrent Neural Network

RNN is normally used in Nature Language Precessing. The input of RNN is normally a set of vectors. If we regard 
monthly data as a vector, we can use RNN to make prediction.

##Model details and performance
|          Model Name          |                    Model Parameters                     | Average Margin of Error |             Evaluation             |
|:----------------------------:|:-------------------------------------------------------:|:-----------------------:|:----------------------------------:|
|          ElasticNet          |               alpha: 0.025 l1_ratio: 1.0                |          19.4%          |       Simple,Fast,Inaccurate       |
|    Support Vector Machine    |                         C: 0.7                          |          11.9%          |       Simple, Fast, Accurate       |
|     KNeighborsRegressor      |                 Number of neighbors: 7                  |          25.3%          | No need to train, Slow, Inaccurate |
|   GaussianProcessRegressor   |                Prior:0 Kernel:DotProduct                |          13.2%          |      Complex, Fast, Accurate       |
|        Decision Tree         | max_depth: 10 min_samples_split: 8  min_samples_leaf: 2 |          12.8%          |       Simple, Fast, Accurate       |
|     Deep Neural Network      |              please review the source code              |          8.3%           |      Complex, Fast, Accurate       |
| Convolutional Neural Network |              please review the source code              |          18.8%          |      Complex, Fast, Accurate       |
|   Recurrent Neural Network   |              please review the source code              |          13.3%          |      Complex, Fast, Accurate       |
