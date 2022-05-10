import numpy as np
import keras.regularizers
import pandas as pd
from sklearn import preprocessing
import sklearn.model_selection
from sklearn.linear_model import LinearRegression
import tensorflow as tf
from tensorflow.keras import layers
import matplotlib.pyplot as plt

raw_data = pd.read_csv('crops_processing_csv_v6.csv', delimiter=',')

areas = ['AUS']
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

required_X_columns = []
required_y_columns = []
for area in areas:
    for month in months:
        required_X_columns.append(area + '_' + month + '_temp')
        required_X_columns.append(area + '_' + month + '_rain')
    required_X_columns.append(area + '_Wheat_Area')
    required_y_columns.append(area + '_Wheat_Production')

X = pd.DataFrame(raw_data[required_X_columns].applymap(lambda x: x.replace(' ', '') if isinstance(x, str) else x),
                 dtype=np.float)
y = pd.DataFrame(raw_data[required_y_columns].applymap(lambda x: x.replace(' ', '') if isinstance(x, str) else x),
                 dtype=np.float).sum(axis=1)

standardize_scaler = preprocessing.MinMaxScaler()
standardize_scaler = standardize_scaler.fit(X)

means = X.mean(axis=0)
future_years_dataset = pd.DataFrame(X)
future_years_dataset = future_years_dataset.drop(index=[0, 1])
np.random.seed(10)
for i in range(len(means)):
    if i == len(means) - 1:
        future_years_dataset.iloc[:, i] = np.random.normal(means[i], 500, size=(30, 1))
    elif i % 2 == 0:
        future_years_dataset.iloc[:, i] = np.random.normal(means[i], 1.5, size=(30, 1))
    else:
        future_years_dataset.iloc[:, i] = np.random.normal(means[i], 25, size=(30, 1))

future_years_dataset_scaled = standardize_scaler.transform(future_years_dataset)

model = tf.keras.models.Sequential([
    layers.Dense(32, kernel_initializer='random_normal', input_shape=(X.shape[1],),
                 kernel_regularizer=keras.regularizers.L2(0.01)),
    layers.BatchNormalization(),
    layers.Activation('relu'),
    layers.Dropout(0.2),
    layers.Dense(8, kernel_initializer='random_normal'),
    # layers.BatchNormalization(),
    layers.Activation('relu'),
    layers.Dropout(0.2),
    layers.Dense(1),
    layers.Activation('relu')

])
model.load_weights('checkpoints/mnist.ckpt')
re = model.predict(future_years_dataset_scaled)
future_years_dataset['wheat_production'] = re * 10000
years = []
for i in range(30):
    years.append(2022 + i)
future_years_dataset.insert(0, 'year', years)
future_years_dataset.to_csv('wheat_production_prediction.csv', index=None)
print()
