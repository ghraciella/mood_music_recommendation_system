"""
script : data_processing.py 
purpose: 


"""

from sklearn.preprocessing import MinMaxScaler, StandardScaler

# Importing necessary libraries and modules for modelling

import subprocess

try:

    import numpy as np
    import pandas as pd
    import random as rnd


    # split data - avoid data leakage
    from sklearn.model_selection import train_test_split


    # cross validation, hyperparameter tuning
    from sklearn.model_selection import GridSearchCV, RandomizedSearchCV 

    # preprocessing, scaling
    from sklearn.preprocessing import MinMaxScaler, StandardScaler
    from sklearn.preprocessing import MinMaxScaler

    # high dimensional usage - dimensionality reduction
    from sklearn.manifold import TSNE
    from sklearn.decomposition import PCA
    from umap import UMAP


    # pipeline
    from sklearn.pipeline import Pipeline
    from sklearn.pipeline import make_pipeline


except ImportError as error:
    print(f"Installation of the required dependencies necessary! {error}")

    subprocess.check_call(["pip", "install", "numpy"])
    subprocess.check_call(["pip", "install", "pandas"])
    subprocess.check_call(["pip", "install", "scikit-learn"])


    print(f"Successful installation of the required dependencies necessary")


import warnings
warnings.filterwarnings('ignore')




# functions
# -- get balanced data
# -- split? function
# -- data scaling - normalizing the data
# -- dimensionality reduction (tsne, umap, pca)
# -- hyperparameter tuning
# -- 







# dataset is unbalanced from the perspective of the associated mood 
#    get the count of how the mood is distributed wrt the data
# get sample size = 15000 #20000

def get_balanced_data(processed_dataset, sample_size = 20000, *args, **kwargs):

    ''' 
    get data with specified sample size based on each mood?
        
    '''

    sampled_moosic_data  = pd.DataFrame()
    grouped_data = processed_dataset.groupby('mood_goal')


    for mood_label, group in grouped_data:
        
        #print(f' getting data samples for the mood : {mood_label} \n ')

        if len(group) >= sample_size: 
            random_rows = group.sample(sample_size, random_state=42) 
        else:
            random_rows = group  

        sampled_moosic_data = pd.concat([sampled_moosic_data, random_rows])

        continue

    print(f' Finished processing, data has balanced number of samples for all categories. ')

    sampled_moosic_data = sampled_moosic_data.reset_index(drop=True) 

    mood_label_counts = sampled_moosic_data['mood_goal'].value_counts()
    print(f"The size of data mood label count {mood_label_counts} ")
    print("______"*10)

    return sampled_moosic_data




# function to split dataset for modelling 
# splitting dataset and also retain specific features to be outputted

def split_dataset(dataset, target_feature = 'mood_goal', input_features = ['track_id', 'valence','energy', 'mood_goal'],  
                        drop_features = ['track_id'], output_features = ['track_id', 'mood_goal'], *args, **kwargs): 
    
    """
    split dataset to avoid data leakage
    
    """

    ## get list of moosic data features
    #features = dataset.columns.tolist()

    # defining X (input feature vectors) and Y (target output features)


    X_data = dataset[input_features]

    y_data = dataset['mood_goal']


    # splitting the dataset into train and test

    X_train, X_test, y_train, y_test = train_test_split(X_data, y_data, test_size=0.20, random_state=42, shuffle=True, stratify=y_data)

    Y_train = X_train[output_features].reset_index(drop=True)
    Y_test = X_test[output_features].reset_index(drop=True)

    X_train = X_train[input_features].drop(drop_features, axis=1).reset_index(drop=True)
    X_test =  X_test[input_features].drop(drop_features, axis=1).reset_index(drop=True)

    y_train = Y_train[target_feature].reset_index(drop=True)
    y_test = Y_test[target_feature].reset_index(drop=True)

    data  = {
        'X_data':X_data,
        'y_data':y_data,
        'X_train':X_train,
        'X_test':X_test,
        'y_train':y_train,
        'y_test':y_test,        
        'Y_train':Y_train,
        'Y_test':Y_test,
        }

    return data




