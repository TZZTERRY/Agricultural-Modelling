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
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.tree import DecisionTreeRegressor

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

hyperparameters_dict = {'max_depth': range(2, 20, 2),
                        'min_samples_split': range(2, 20, 2),
                        'min_samples_leaf': range(2, 20, 2)}
min_error = 1000
kf = KFold(n_splits=5, random_state=10, shuffle=True)

best_parameter = {'max_depth': 0,
                  'min_samples_split': 0,
                  'min_samples_leaf': 0}

for max_depth in hyperparameters_dict['max_depth']:
    for min_samples_split in hyperparameters_dict['min_samples_split']:
        for min_samples_leaf in hyperparameters_dict['min_samples_leaf']:
            dt = DecisionTreeRegressor(max_depth=max_depth,
                                       min_samples_split=min_samples_split,
                                       min_samples_leaf=min_samples_leaf)

            cv_results = cross_validate(dt, X, y, cv=kf, scoring='neg_mean_squared_error', return_train_score=True,
                                        return_estimator=True)
            if np.mean(np.abs(cv_results['test_score'])) < min_error:
                best_parameter['max_depth'] = max_depth
                best_parameter['min_samples_split'] = min_samples_split
                best_parameter['min_samples_leaf'] = min_samples_leaf
                min_error = np.mean(np.abs(cv_results['test_score']))

best_model = DecisionTreeRegressor(max_depth=best_parameter['max_depth'],
                                   min_samples_split=best_parameter['min_samples_split'],
                                   min_samples_leaf=best_parameter['min_samples_leaf']).fit(X, y)

error = (best_model.predict(X) - y) / y
mean_error = np.mean(np.abs(error))
print('DCT: para: {a}, error {b}'.format(a=best_parameter, b=mean_error))
