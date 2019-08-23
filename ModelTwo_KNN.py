import numpy as np; import pandas as pd; import math; import operator;from sklearn.neighbors import KNeighborsClassifier; from imblearn.over_sampling import SMOTE
from sklearn.metrics import accuracy_score; from sklearn.model_selection import train_test_split; from sklearn.preprocessing import StandardScaler
from sklearn.metrics import roc_auc_score
from sklearn.metrics import roc_curve; import matplotlib.pyplot as plt; import misc

   
def KNN(X_train,X_test,y_train,y_test,size):
    #number of neighbors recommended size should be sqrt(number of obs)
    #make sure X vectors are standarized or normalized and balanced, make sure y train is balanced so that you get sounds results.
    n = int(math.ceil(size**(1/2)))
    knn = KNeighborsClassifier(n_neighbors = n)
    knn.fit(X_train,y_train)
    prediction = knn.predict(X_test)
    score = accuracy_score(y_test,prediction)
    print(score)
    return score, knn,prediction

if __name__=='__main__':
    df = pd.read_csv('data/PopulationDataSet_NotStandardized.csv', header=0) 
    size = len(df) 
    X_train_stdb,X_test_std,y_train_b,y_test= misc.preprocess(df)
    score,knn,prediction = KNN(X_train_stdb,X_test_std,y_train_b,y_test,size) 
    misc.visualize(knn,prediction,y_test,X_test_std)
