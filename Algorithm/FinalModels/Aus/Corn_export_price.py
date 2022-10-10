import numpy as np
import keras.regularizers
import pandas as pd
from sklearn import preprocessing
import tensorflow as tf
from tensorflow.keras import layers

# Load and process data
raw_data = pd.read_csv('data/AUS_v5.csv', delimiter=',')
areas = ['AUS']
required_X_columns = []
required_y_columns = []
required_X_columns.append('Covid')
required_X_columns.append('Oil_Price')
required_X_columns.append('Corn_Production')
required_X_columns.append('America_Corn_production')
required_X_columns.append('America_Corn_export_volume')
required_X_columns.append('America_Corn_trade_value')
required_X_columns.append('Asia_Corn_production')
required_X_columns.append('Asia_Corn_export_volume')
required_X_columns.append('Asia_Corn_trade_value')
required_X_columns.append('Europe_Corn_production')
required_X_columns.append('Europe_Corn_export_volume')
required_X_columns.append('Europe_Corn_trade_value')
required_X_columns.append('Oceania_Corn_production')
required_X_columns.append('Oceania_Corn_export_volume')
required_X_columns.append('Oceania_Corn_trade_value')
required_y_columns.append('Corn_export_price')
raw = raw_data[required_X_columns].applymap(lambda x: x.replace(' ', '') if isinstance(x, str) else x)
raw = raw.applymap(lambda x: x.replace(',', '') if isinstance(x, str) else x)
X = pd.DataFrame(raw, dtype=np.float)
y = pd.DataFrame(raw_data[required_y_columns].applymap(lambda x: x.replace(' ', '') if isinstance(x, str) else x),
                 dtype=np.float).sum(axis=1)
standardize_scaler = preprocessing.MinMaxScaler()
X = standardize_scaler.fit_transform(X)

# Build the model
model = tf.keras.models.Sequential([
    layers.Dense(32, kernel_initializer='random_normal', input_shape=(X.shape[1],),
                 kernel_regularizer=keras.regularizers.L2(0.01)),
    layers.BatchNormalization(),
    layers.Activation('relu'),
    layers.Dense(64, kernel_initializer='random_normal'),
    layers.Activation('relu'),
    layers.Dense(1),
    layers.Activation('relu')
])
check_points_path = 'checkpoints_corn_export_price/model.ckpt'

# Uncomment this block when retraining the model(do not do this without permission)
# cp_checkpoint_callback = tf.keras.callbacks.ModelCheckpoint(filepath=check_points_path, save_weights_only=True,
#                                                             save_best_only=True)
# model.compile(optimizer='adam', loss='mse')
# history = model.fit(x=X, y=y.values, batch_size=5, epochs=3000, validation_split=0.1,
#                     callbacks=[cp_checkpoint_callback])
# Show the result
model.load_weights(check_points_path)
re = model.predict(X)
dif = (np.reshape(re, (32,)) - y.values) / y.values
m = np.mean(np.abs(dif))
print('Average margin of error: {m}'.format(m = m))
years = []
for i in range(32):
    years.append(1990 + i)
result = pd.DataFrame({'Year':years,'Prediction value': np.reshape(re, (32,)), 'Actual value': y.values, 'Margin of error(%)': np.abs(dif*100)})
print(result)

# 0.12488556995723815



