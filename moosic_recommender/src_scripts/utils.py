"""
script : data_processing.py 
purpose: 


"""


# Importing necessary libraries and modules for modelling

import subprocess

try:

    import numpy as np
    import pandas as pd
    import random as rnd


    # split data - avoid data leakage
    from sklearn.model_selection import train_test_split, cross_val_score

    # cross validation, hyperparameter tuning
    from sklearn.model_selection import GridSearchCV, RandomizedSearchCV 

    # preprocessing, scaling
    from sklearn.preprocessing import MinMaxScaler, StandardScaler

    # pipeline
    from sklearn.pipeline import Pipeline


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
# -







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








def cross_validation(X_data, y_data, method='randomsearch', param_grid= None, cv=5, n_iter=10,
                        param_distributions= None, estimator= None, random_state= 42,  n_jobs=-1, *args, **kwargs):


    """
    Model (estimator) selection : cross validation and hyperparameter tuning
        - cross_val_score
        - gridsearchcv
        - randomsearchcv
        - stratified kfold


    """

    cv_search_methods = {
        'cross_val_score': cross_val_score(estimator, param_grid, cv=cv, n_jobs=n_jobs),
        'gridsearch': GridSearchCV(estimator, param_grid, cv=cv, n_jobs=n_jobs),
        'randomsearch': RandomizedSearchCV(estimator, param_distributions, cv=cv, n_iter=n_iter, n_jobs=n_jobs),
        #'stratifiedkfold': StratifiedKFold(n_splits=2, random_state=random_state)

    }

    if method in cv_search_methods:
        cv_search = cv_search(estimator, param_grid, cv=cv, n_jobs=n_jobs)
        cv_search.fit(X_data, y_data)
        return cv_search.best_params_, cv_search.best_score_ 
    else:
        raise ValueError(f" The CV technique '{method}' for hyperparameter search is not supported.")






