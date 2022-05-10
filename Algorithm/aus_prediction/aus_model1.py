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
X = standardize_scaler.fit_transform(X)
y = y / 10000

# X_train,X_validation,y_train,y_validation = sklearn.model_selection.train_test_split(X,y,train_size=0.1,random_state=1)
# model = LinearRegression().fit(X_train,y_train)
# print(model.score(X_validation,y_validation))

model = tf.keras.models.Sequential([
    layers.Dense(32, kernel_initializer='random_normal', input_shape=(X.shape[1],),
                 kernel_regularizer=keras.regularizers.L2(0.01)),
    layers.BatchNormalization(),
    layers.Activation('relu'),
    layers.Dropout(0.2),
    layers.Dense(8, kernel_initializer='random_normal'),
    layers.Activation('relu'),
    layers.Dropout(0.2),
    layers.Dense(1),
    layers.Activation('relu')

])
model.load_weights('checkpoints/mnist.ckpt')

# Uncomment this if you are going to check the performance of the model(check result variable)
# re = model.predict(X)
# dif = (np.reshape(re, (32,)) - y.values) / y.values
# m = np.mean(np.abs(dif))
# years = []
# for i in range(32):
#     years.append(1990 + i)
# result = pd.DataFrame({'Year':years,'Prediction value': np.reshape(re, (32,)), 'Actual value': y.values, 'Margin of error(%)': np.abs(dif*100)})
# print(result)

# Uncomment this block when retraining the model(do not do this without permission)
# check_points_path = 'checkpoints2/mnist.ckpt'
# cp_checkpoint_callback = tf.keras.callbacks.ModelCheckpoint(filepath=check_points_path, save_weights_only=True,
#                                                             save_best_only=True)
# model.compile(optimizer='adam', loss='mse', metrics=['mae', 'mse'])
#
# history = model.fit(x=X, y=y.values, batch_size=5, epochs=10000, validation_split=0.2,
#                     callbacks=[cp_checkpoint_callback])

# acc = history.history['accuracy']
# val_acc = history.history['val_accuracy']
# loss = history.history['loss']
# val_loss = history.history['val_loss']
# print('val loss : %s'%np.min(val_loss))
#
# plt.subplot(1, 2, 1)
# plt.plot(acc, label='Training Accuracy')
# plt.plot(val_acc, label='Validation Accuracy')
# plt.title('Training and Validation Accuracy')
# plt.legend()
#
# plt.subplot(1, 2, 2)
# plt.plot(loss, label='Training Loss')
# plt.plot(val_loss, label='Validation Loss')
# plt.title('Training and Validation Loss')
# plt.legend()
#
# plt.show()
