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

    import re

    import nltk
    nltk.download('stopwords')
    from nltk.corpus import stopwords
    from nltk.cluster import KMeansClusterer

    # object serialization
    import joblib


    # split data - avoid data leakage
    from sklearn.model_selection import train_test_split, cross_val_score


    # cross validation, hyperparameter tuning
    from sklearn.model_selection import GridSearchCV, RandomizedSearchCV, StratifiedKFold 

    # preprocessing: scaling, encoding
    from sklearn.preprocessing import MinMaxScaler, StandardScaler, OneHotEncoder, LabelEncoder
    from sklearn.compose import ColumnTransformer



except ImportError as error:
    print(f"Installation of the required dependencies necessary! {error}")

    subprocess.check_call(["pip", "install", "numpy"])
    subprocess.check_call(["pip", "install", "pandas"])
    subprocess.check_call(["pip", "install", "scikit-learn"])


    print(f"Successful installation of the required dependencies necessary")


import warnings
warnings.filterwarnings('ignore')


# custom imports


from .dataloader import (
                load_data,
        )

from .data_processing import (
        data_preprocessor, 
        dimensionality_reduction, 
        cross_validation,
        )

from .feature_engineering import (
        mood_quadrant_map, 
        mood_1d_map, 
        mood_2d_map,
        mood_3d_map,
        )

from .models import (
    text_processing,
    )

from .tests import (
        get_invalid_indicies, 
        )



# functions
# -- data scaling - normalizing the data
# -- Model selection : cross validation and hyperparameter tuning
# -- 






def data_wrangling(data):

    """

    :param data: object - data
    :return: object - data

    Description:

    data wrangling : cleaning, imputation, transformations and feature engineering
        - drop duplicates
        - removing punctuation and special characters
        - drop observations (rows) where 'ValueError' occurs


    feature engineering
        - target feature engineering : mood
        - core genre labels

    tokenization
        - tokenization of genre : break 



    """


    data = data.drop_duplicates()

    data = data.applymap(lambda text: re.sub(r'[^A-Za-z0-9]+', ' ', text))
    data = data[data['genres'].str.contains(r'podcast|podcasts', case=False)]


    data = data.copy(deep=True)
    data = data.query("main_genres != '[]' ").reset_index(drop=True)
    data = data.convert_dtypes()
    null_rows = data[data.isnull().T.any()].index
    data = data.drop(null_rows)

    print(data.isnull().T.any())


    data['mood_quadrants'] = data.apply(mood_quadrant_map , axis=1)
    data['mood_label_1d'] = data.apply(mood_1d_map, axis=1)
    data['mood_label_2d'] = data.apply(mood_2d_map, axis=1)

    error_indices = get_invalid_indicies(data, mood_quadrant_map)
    data = data.drop(error_indices)


    return data




def save_data_embeddings(data, data_path, file_path, file_name='moosic_data_embedding', *args, **kwargs):

    """


    :param data: object - data
    :param data_path: str - path to data
    :param file_path: str - path/location to save embedded data file
    :param file_name: str - save file with the name
    :print: str - print statement of sucessful save

    Description:

    generate and save processed data as embedding : cleaning, imputation, transformations and feature engineering
        - using joblib
        - or pickle?


    """
    
    get_embeddings = load_data(data_path=data_path, source='flat')
    data_embeddings = get_embeddings.values
    joblib.dump(data_embeddings, file_path)

    print(f"The file {file_name} sucessefully saved to location: {file_path}")




def get_balanced_data(processed_dataset, sample_size = 20000, *args, **kwargs):

    ''' 
    get data with specified sample size based on each mood?


    :param processed_dataset: object - processed data
    :param sample_size: int - numeric value for size of data samples
    :return: object - data

    Description:

    get the count of how the mood is distributed wrt the data
        - count of tracks by each mood
        - get mood label with lowest count
        - group the data based on the mood labels (mood_goal of tracks for user)
        - get dataset with randomly selected track samples for each mood labels based on 
        the value from the least occuring mood label
        
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





def data_scaler_encoder(data, scaler = 'minmax', *args, **kwargs):

    """


    :param data: object - data
    :param scaler: str - scaling/encoding method 
    :return: object - scaled/encoded data

    Description:

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


    :param data: object - data
    :param data_type: str - data type i.e 'num' (numerical) or 'cat' (categorical) 
    :param scaler: str - scaling/encoding method
    :return: object - processed data

    Description:

    num: scaling our numerical data
    cat: encoding our numerical data
    
    """

    if not isinstance(data_type, str) and (data_type not in ('num', 'cat')):

        raise ValueError('''Incorrect entry for the data_type to be preprocessed. 
                        Provide valid input: 'cat' for categorical data and 'num' for numerical data ''')
    
    else:

        if data_type == 'num' and scaler in ('minmax', 'standard'):
            # for preprocessing / scaling our numerical data
            scaled_data = data_scaler_encoder(data, scaler=scaler)


        elif data_type == 'cat' and scaler in ('label', 'onehot'):
            # for preprocessing / encoding our numerical data
            scaled_data = data_scaler_encoder(data, scaler=scaler)
        
        else:
            raise ValueError('''Incorrect scaler for the data_type to be preprocessed.Provide valid 
                            input: categorical data ('label' or 'onehot') and for numerical data  ('minmax' or 'standard')''')
        


    return scaled_data







# function to split dataset for modelling 
# splitting dataset and also retain specific features to be outputted

def split_dataset(dataset, target_feature = 'mood_goal', input_features = ['track_id', 'valence','energy', 'mood_goal'],  
                        drop_features = ['track_id'], output_features = ['track_id', 'mood_goal'], *args, **kwargs): 
    
    """
    split dataset to avoid data leakage


    :param dataset: object - 
    :param target_feature: str - target feauture 
    :param input_features: str - input feauture 
    :param drop_features: str - feautures to be dropped 
    :param output_features: str - output features
    :return: object - dictionary of split data

    Description:

    
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











def data_pipeline(data_path):

    """

    :param data_path: str - path to data
    :return:  


    moosic data pipeline
        - extract and load data
        - data_transformations : wrangling
        - target feature engineering : mood and genre
        - avoiding data leakage : train-test-split data
        - getting balanced data
        - data scaling : normalisation of numerical data, encoding of categorical data

        - text preprocessing e.g tf-idf, tokenization, removing stopwords, stemming


    """





    pass 
















