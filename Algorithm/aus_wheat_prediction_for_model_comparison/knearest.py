import numpy as np
import keras.regularizers
import pandas as pd
from sklearn import preprocessing
import sklearn.model_selection
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import ElasticNet
from sklearn.model_selection import cross_validate
from sklearn.model_selection import KFold
from sklearn import svm
from sklearn.neighbors import KNeighborsRegressor


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

kf = KFold(n_splits=5, random_state=10, shuffle=True)
min_error = 100
best_para = {}
for N in np.arange(1,21):
    model = KNeighborsRegressor(N)
    cv_result = cross_validate(model, X, y, scoring='neg_mean_squared_error', cv=kf.split(X),
                               return_train_score=True,
                               return_estimator=True)
    e = np.mean(np.abs(cv_result['test_score']))
    if e < min_error:
        best_para['N'] = N
        min_error = e

best_model = KNeighborsRegressor(best_para['N']).fit(X, y)

error = (best_model.predict(X) - y) / y
mean_error = np.mean(np.abs(error))
print('Knearst: para: {a}, error {b}'.format(a=best_para, b=mean_error))
