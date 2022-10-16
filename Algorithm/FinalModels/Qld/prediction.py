import numpy as np
import keras.regularizers
import pandas as pd
from sklearn import preprocessing
import sklearn.model_selection
from sklearn.linear_model import LinearRegression
import tensorflow as tf
from tensorflow.keras import layers
import matplotlib.pyplot as plt

raw_data = pd.read_csv('data/Qld_v5.csv', delimiter=',')

areas = ['NSW']
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
required_X_columns = []
required_y_columns = []
for month in months:
    required_X_columns.append(month + '_temp')
    required_X_columns.append(month + '_rain')
    required_X_columns.append(month + '_humidity')
    required_X_columns.append(month + '_wind')
    required_X_columns.append(month + '_uva')
    required_X_columns.append(month + '_uvb')
    required_X_columns.append(month + '_eva')
required_X_columns.append('Barley_Area')
required_X_columns.append('Covid')
required_y_columns.append('Barley_Production')
raw = raw_data[required_X_columns].applymap(lambda x: x.replace(' ', '') if isinstance(x, str) else x)
raw = raw.applymap(lambda x: x.replace(',', '') if isinstance(x, str) else x)
X = pd.DataFrame(raw, dtype=np.float)
y = pd.DataFrame(raw_data[required_y_columns].applymap(lambda x: x.replace(' ', '') if isinstance(x, str) else x),
                 dtype=np.float).sum(axis=1)

standardize_scaler = preprocessing.MinMaxScaler()
standardize_scaler = standardize_scaler.fit(X)

means = X.mean(axis=0)
future_years_dataset = pd.DataFrame(X)
future_years_dataset = future_years_dataset.drop(index=[0, 1])
np.random.seed(10)
for i in range(len(means)):
    future_years_dataset.iloc[:, i] = np.random.normal(means[i], means[i] / 50, size=(30, 1))

future_years_dataset['Covid'] = np.ones(future_years_dataset.shape[0])
future_years_dataset_scaled = standardize_scaler.transform(future_years_dataset)


model = tf.keras.models.Sequential([
    layers.Dense(32, kernel_initializer='random_normal', input_shape=(X.shape[1],),
                 kernel_regularizer=keras.regularizers.L2(0.01)),
    layers.BatchNormalization(),
    layers.Activation('relu'),
    layers.Dense(64),
    layers.Activation('relu'),
    layers.Dense(128),
    layers.Activation('relu'),
    layers.Dense(1),
    layers.Activation('relu')
])
check_points_path = 'checkpoints_barley_yield/model.ckpt'
model.load_weights(check_points_path)
re = model.predict(future_years_dataset_scaled)
future_years_dataset['Barley_Production'] = re
years = []
for i in range(30):
    years.append(2022 + i)
future_years_dataset.insert(0, 'year', years)
future_years_dataset.to_csv('prediction_result/Qld_Barley_Production_prediction.csv', index=None)
print()
