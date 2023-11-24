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
    from sklearn.model_selection import train_test_split, cross_val_score


    # cross validation, hyperparameter tuning
    from sklearn.model_selection import GridSearchCV, RandomizedSearchCV, StratifiedKFold 

    # preprocessing, scaling
    from sklearn.preprocessing import MinMaxScaler, StandardScaler

    # high dimensional usage - dimensionality reduction
    from sklearn.manifold import TSNE
    from sklearn.decomposition import PCA
    from umap import UMAP



except ImportError as error:
    print(f"Installation of the required dependencies necessary! {error}")

    subprocess.check_call(["pip", "install", "numpy"])
    subprocess.check_call(["pip", "install", "pandas"])
    subprocess.check_call(["pip", "install", "scikit-learn"])
    subprocess.check_call(["pip", "install", "umap-learn"])


    print(f"Successful installation of the required dependencies necessary")


import warnings
warnings.filterwarnings('ignore')




# functions
# -- data scaling - normalizing the data
# -- dimensionality reduction (tsne, umap, pca)
# -- Model selection : cross validation and hyperparameter tuning
# -- 





def data_scaling_normalization(X_data, scaler = 'min_max', *args, **kwargs):

    """
    scaling the data
        - normalization : minmaxscaler
        - standardization : standardscaler
    
    """

    scalers = {
        'min_max': MinMaxScaler(),
        'standard': StandardScaler()
    }

    if scaler in scalers:
        scaler = scalers[scaler]
        return scaler.fit_transform(X_data)
    else:
        raise ValueError(f"The scaling - normalization technique: '{scaler}' is not supported.")


def dimensionality_reduction(dataset, method='tsne', n_components=2, random_state=42, *args, **kwargs):

    """
    Dimensionality reduction techniques

    """

    methods = {
        'pca': PCA(n_components=n_components, random_state=random_state),
        'tsne': TSNE(n_components=n_components, random_state=random_state),
        'umap': UMAP(n_components=n_components, random_state=random_state)
    }

    if method in methods:
        reduction_method = methods[method]
        return reduction_method.fit_transform(dataset)
    else:
        raise ValueError(f"The dimensionality reduction technique: '{method}' is currently not available.")




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





















