import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error


def predictor(data):
    heera = pd.read_csv('diamonds.csv')
    heera['cut'].replace(['Ideal', 'Premium', 'Good', 'Very Good', 'Fair'], [0,1,2,3,4], inplace=True)
    heera['clarity'].replace(['IF', 'VVS1', 'VVS2', 'VS1', 'VS2', 'SI1', 'SI2', 'I1'], [0,1,2,3,4,5,6,7], inplace=True)
    heera['color'].replace(['D', 'E', 'F', 'G', 'H', 'I', 'J'], [0,1,2,3,4,5,6], inplace=True)
    # heera.drop(['Unnamed: 0.1','Unnamed: 0.1'], axis=1,inplace=True)
    X = heera[['x','y','z','carat','color','clarity','depth','table']].values
    y = heera["price"].values
    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.4,random_state=0)
    knn = KNeighborsRegressor(n_neighbors = 2)
    knn.fit(X_train,y_train)
    prediction = knn.predict(data)[0]
    return prediction