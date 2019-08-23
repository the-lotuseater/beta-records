import numpy as np; import pandas as pd; import math; import operator;from sklearn.neighbors import KNeighborsClassifier; from imblearn.over_sampling import SMOTE
from sklearn.metrics import accuracy_score; from sklearn.model_selection import train_test_split; from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier; import misc
from sklearn.metrics import roc_auc_score
from sklearn.metrics import roc_curve; import matplotlib.pyplot as plt
    
def randomforest(X_train,X_test,y_train):    
    """
    Input:Standardized (and possibly balanced) training vectors, testing vectors
    Output: The randomforest model and the accuracy score of the model
    Behaviour:Creates a Random Forest
    """
    forest = RandomForestClassifier(n_estimators = 400)
    forest.fit(X_train,y_train)
    prediction = forest.predict(X_test)
    return forest, prediction
   
if __name__ =='__main__':
    df = pd.read_csv('data/PopulationDataSet_NotStandardized.csv')
    X_train,X_test,y_train,y_test = misc.preprocess(df) 
    model,prediction = randomforest(X_train,X_test,y_train)
    print(accuracy_score(y_test,prediction))
    misc.visualize(model,prediction,y_test,X_test)
