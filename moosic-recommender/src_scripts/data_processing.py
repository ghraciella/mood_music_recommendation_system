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
    from sklearn.model_selection import GridSearchCV, RandomizedSearchCV, StratifiedKFold 

    # preprocessing: scaling, encoding
    from sklearn.preprocessing import MinMaxScaler, StandardScaler, OneHotEncoder, LabelEncoder
    from sklearn.compose import ColumnTransformer

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





def data_scaling_normalization(data, scaler = 'minmax', *args, **kwargs):

    """
    scaling the data
        - normalization : minmaxscaler
        - standardization : standardscaler
    
    """

    scalers = {
        'minmax': MinMaxScaler(),
        'standard': StandardScaler(),
        'label': LabelEncoder(),
        'onehot': OneHotEncoder() 
    }

    if scaler in scalers:
        scaler = scalers[scaler]
        return scaler.fit_transform(data)
    else:
        raise ValueError(f"The scaling - normalization technique: '{scaler}' is not supported.")



def data_preprocessor(data, data_type = 'num', scaler= 'onehot', *args, **kwargs):

    """"
    num: scaling our numerical data
    cat: encoding our numerical data
    
    """

    if not isinstance(data_type, str) and (data_type not in ('num', 'cat')):

        raise ValueError('''Incorrect entry for the data_type to be preprocessed. 
                        Provide valid input: 'cat' for categorical data and 'num' for numerical data ''')
    
    else:

        if data_type == 'num' and scaler in ('minmax', 'standard'):
            # for preprocessing / scaling our numerical data
            scaled_data = data_scaling_normalization(data, scaler=scaler)


        elif data_type == 'cat' and scaler in ('label', 'onehot'):
            # for preprocessing / encoding our numerical data
            scaled_data = data_scaling_normalization(data, scaler=scaler)
        
        else:
            raise ValueError('''Incorrect scaler for the data_type to be preprocessed.Provide valid 
                            input: categorical data ('label' or 'onehot') and for numerical data  ('minmax' or 'standard')''')
        


    return scaled_data


### column transformer pieline



def dimensionality_reduction(data, method='tsne', n_components=2, random_state=42, *args, **kwargs):

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
        return reduction_method.fit_transform(data)
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





















