
"""
script : feature_engineering.py 
purpose: 


"""


# Importing necessary libraries and modules for modelling

import subprocess

try:

    import numpy as np
    import pandas as pd

    import re
    import nltk



except ImportError as error:
    print(f"Installation of the required dependencies necessary! {error}")

    subprocess.check_call(["pip", "install", "numpy"])
    subprocess.check_call(["pip", "install", "pandas"])


    print(f"Successful installation of the required dependencies necessary")


import warnings
warnings.filterwarnings('ignore')


# custom imports
from .tests import (
        get_invalid_indicies, 
        )








def mood_mapper(data, mood_map_dict, mood_features = ['valence', 'energy'], *args, **kwargs):
    """ 
    Mood labels feature engineering 
        quadrants and sub-quadrants affect terms (label) creation  based on features

    :param data: object - data
    :param mood_map_dict: dict object - dictionary containing mood based key-value pairs to be mapped
    :param mood_features: list object - list of mood features to check condition on data to be labeled    
    :return: object - data

    Description:

    Function to map mood (affect) terms based on range of tuple values
    it is associated with.

    The list of tuples represents the core 4 mood quadrants and 8 moods sub-quadrants 

    Mood terms and values example:
        - 'mood term' : tuple | list of tuples


    """

    if isinstance(mood_map_dict, dict):
        mood_map_base = mood_map_dict
    else:
        raise ValueError(''' Function requires a dictionary mapping mood term to values in tuple or list of tuples ''')

    for feature in mood_features:
        feature_data = data[feature]
        if not all(0 <= val <= 1 for val in feature_data):
            raise ValueError(f''' Values for valence and energy must be between 0 and 1.
                            Mood term can't be assigned for these values of the feature column={feature}''')
    
    mood_labels = np.select(list(mood_map_base.values()), list(mood_map_base.keys()), default='unknown')

    return mood_labels



def mood_quadrant_map(data):

    features = ['valence', 'energy']

    quadrant_map = {
        'Q1': (0.5 <= data[features[0]]) & (data[features[0]] <= 1.0) & (0.5 <= data[features[1]]) & (data[features[1]] <= 1.0),
        'Q2': (0.0 <= data[features[0]]) & (data[features[0]] <= 0.5) & (0.5 <= data[features[1]]) & (data[features[1]] <= 1.0),
        'Q3': (0.0 <= data[features[0]]) & (data[features[0]] <= 0.5) & (0.0 <= data[features[1]]) & (data[features[1]] <= 0.5),
        'Q4': (0.5 <= data[features[0]]) & (data[features[0]] <= 1.0) & (0.0 <= data[features[1]]) & (data[features[1]] <= 0.5)
    }
    labels = mood_mapper(data, quadrant_map, features)

    return labels

def mood_quadrant_map(data):
    """ 
    Mood quadrant feature engineering (4 Quadrants)
        VE 2D circumplex model : valence, energy

    :param data: object - data
    :return: object - data

    Description:

    Function to map mood (affect) quadrants to terms based on the valence and energy values
    it is associated with

    Mood quadrant terms and values : 
        - 'happy' : high valence, high energy [(0.5, 1.0), (0.5, 1.0)]
        - 'tense' : low valence, high energy [(0.0, 0.5), (0.5, 1.0)]
        - 'sad' : low valence, low energy [(0.0, 0.5), (0.0, 0.5)]
        - 'relaxed' : high valence, low energy [(0.5, 1.0), (0.0, 0.5)]

    - Sub-quadrants (our modified-russell-thayer): 
        - Q1 (Happy)  : M1 - happy [(0.5, 1.0), (0.5, 0.75)],  M2 - euphoric [(0.5, 1.0), (0.75, 1.0)] 
        - Q2 (Tense)  : M3 - tense [(0.0, 0.5), (0.75, 1.0)],  M4 - angry [(0.0, 0.5), (0.5, 0.75)]
        - Q3 (Sad) : M5 - depressive [(0.0, 0.5), (0.25, 0.5)],  M6 - sad [(0.0, 0.5), (0.0, 0.25)]
        - Q4 (Relaxed)  : M7 - calm [(0.5, 1.0), (0.0, 0.25)],  M8 - relaxed [(0.5, 1.0), (0.0, 0.25)]
    
    """

    features = ['valence', 'energy']

    quadrant_map = {
        'Q1': (data[features[0]] <= 0.5 ) & (data[features[0]] <= 1.0) & (0.5 <= data[features[1]]) & (data[features[1]] <= 1.0),
        'Q2': (data[features[0]] <= 0.0) & (data[features[0]] <= 0.5) & (0.5 <= data[features[1]]) & (data[features[1]] <= 1.0),
        'Q3': (data[features[0]] <= 0.0) & (data[features[0]] <= 0.5) & (0.0 <= data[features[1]]) & (data[features[1]] <= 0.5),
        'Q4': (data[features[0]]  <= 0.5) & (data[features[0]] <= 1.0) & (0.0 <= data[features[1]]) & (data[features[1]] <= 0.5)
    }
    
    labels = mood_mapper(data, quadrant_map, features)

    return labels



def mood_1d_map(data):
    """ 
    Mood feature engineering (1D)
        V affect terms : valence

    :param data: object - data
    :return: object - data

    Description:

    Function to map mood (affect) terms based on the valence values
    it is associated with.

    The list of tuples represents the core 8 moods dominate based on valence.

    Mood terms and values:
        - 'happy' : (0.875, 1.0)
        - 'euphoric' : (0.75, 0.875)                
        - 'tense' : (0.375, 0.5)
        - 'angry' :(0.25, 0.375)
        - 'depressed' : (0.0, 0.125)
        - 'sad' :(0.125, 0.25)
        - 'calm' : (0.5, 0.625)
        - 'relaxed' : (0.625, 0.75)    

    """

    features = ['valence']

    mood_map_1D = {
        'happy': (data[features[0]] > 0.875) & (data[features[0]] <= 1.0),
        'euphoric': (data[features[0]] > 0.75) & (data[features[0]] <= 0.875),
        'tense': (data[features[0]] > 0.375) & (data[features[0]] <= 0.5),
        'angry': (data[features[0]] > 0.25) & (data[features[0]] <= 0.375),
        'depressed': (data[features[0]] > 0.0) & (data[features[0]] <= 0.125),
        'sad': (data[features[0]]> 0.125) & (data[features[0]] <= 0.25),
        'calm': (data[features[0]] > 0.5) & (data[features[0]] <= 0.625),
        'relaxed': (data[features[0]] > 0.625) & (data[features[0]] <= 0.75),        
    }


    mood_labels = mood_mapper(data, mood_map_1D, features)

    return mood_labels



def mood_2d_map(data):
    """ 
    Mood labels feature engineering (2D)
        VE affect terms : valence, energy

    :param data: object - data
    :return: object - data

    Description:

    Function to map mood (affect) terms based on the valence and energy values
    it is associated with.

    The list of tuples represents the core 8 moods (or the 2d cartesian plot) based on valence and energy.

    Mood terms and values:
        - 'happy' : [(0.5, 1.0), (0.5, 0.75)]
        - 'euphoric' : [(0.5, 1.0), (0.75, 1.0)]                
        - 'tense' : [(0.0, 0.5), (0.75, 1.0)]
        - 'angry' : [(0.0, 0.5), (0.5, 0.75)]
        - 'depressed' : [(0.0, 0.5), (0.25, 0.5)]
        - 'sad' : [(0.0, 0.5), (0.0, 0.25)]
        - 'calm' : [(0.5, 1.0), (0.0, 0.25)]
        - 'relaxed' : [(0.5, 1.0), (0.25, 0.5)]    

    
    """

    features = ['valence', 'energy']


    mood_map_2D = {
        'happy': (data[features[0]] >= 0.5) & (data[features[0]] <= 1.0) & (data[features[1]] >= 0.5) & (data[features[1]] <= 0.75),
        'euphoric': (data[features[0]] >= 0.5) & (data[features[0]] <= 1.0) & (data[features[1]] >= 0.75) & (data[features[1]] <= 1.0),
        'tense': (data[features[0]] >= 0.0) & (data[features[0]] <= 0.5) & (data[features[1]] >= 0.75) & (data[features[1]] <= 1.0),
        'angry': (data[features[0]] >= 0.0) & (data[features[0]] <= 0.5) & (data[features[1]] >= 0.5) & (data[features[1]]<= 0.75),
        'depressed': (data[features[0]] >= 0.0) & (data[features[0]] <= 0.5) & (data[features[1]] >= 0.25) & (data[features[1]] <= 0.5),
        'sad': (data[features[0]] >= 0.0) & (data[features[0]] <= 0.5) & (data[features[1]] >= 0.0) & (data[features[1]] <= 0.25),
        'calm': (data[features[0]] >= 0.5) & (data[features[0]] <= 1.0) & (data[features[1]] >= 0.0) & (data[features[1]] <= 0.25),
        'relaxed': (data[features[0]] >= 0.5) & (data[features[0]] <= 1.0) & (data[features[1]] >= 0.25) & (data[features[1]] <= 0.5),       
    }


    mood_labels = mood_mapper(data, mood_map_2D, features)

    return mood_labels




def mood_3d_map(data):
    """ 
    Mood labels feature engineering (3D)
        VED affect terms : valence, energy, danceability

    :param data: object - data
    :return: object - data

    Description:

    Function to map mood (affect) terms based on the valence, energy and danceability values
    it is associated with.

    The list of tuples represents the core 8 moods sub-quadrants 
    (in the 2d cartesian plot) based on valence, energy and danceability.

    Mood terms and values:
        - 'happy' : [(0.5, 1.0, d), (0.5, 0.75, d)]
        - 'euphoric' : [(0.5, 1.0, d), (0.75, 1.0, d)]                
        - 'tense' : [(0.0, 0.5, d), (0.75, 1.0, d)]
        - 'angry' : [(0.0, 0.5, d), (0.5, 0.75, d)]
        - 'depressed' : [(0.0, 0.5, d), (0.25, 0.5, d)]
        - 'sad' : [(0.0, 0.5, d), (0.0, 0.25, d)]
        - 'calm' : [(0.5, 1.0, d), (0.0, 0.25, d)]
        - 'relaxed' : [(0.5, 1.0, d), (0.25, 0.5, d)]    


    """

    features = ['valence', 'energy', 'danceability']

    mood_map_3D = {
        'happy': (data[features[0]] >= 0.5) & (data[features[0]] <= 1.0) & (data[features[1]] >= 0.5) & (data[features[1]] <= 0.75),
        'euphoric': (data[features[0]] >= 0.5) & (data[features[0]] <= 1.0) & (data[features[1]] >= 0.75) & (data[features[1]] <= 1.0),
        'tense': (data[features[0]] >= 0.0) & (data[features[0]] <= 0.5) & (data[features[1]] >= 0.75) & (data[features[1]] <= 1.0),
        'angry': (data[features[0]] >= 0.0) & (data[features[0]] <= 0.5) & (data[features[1]] >= 0.5) & (data[features[1]]<= 0.75),
        'depressed': (data[features[0]] >= 0.0) & (data[features[0]] <= 0.5) & (data[features[1]] >= 0.25) & (data[features[1]] <= 0.5),
        'sad': (data[features[0]] >= 0.0) & (data[features[0]] <= 0.5) & (data[features[1]] >= 0.0) & (data[features[1]] <= 0.25),
        'calm': (data[features[0]] >= 0.5) & (data[features[0]] <= 1.0) & (data[features[1]] >= 0.0) & (data[features[1]] <= 0.25),
        'relaxed': (data[features[0]] >= 0.5) & (data[features[0]] <= 1.0) & (data[features[1]] >= 0.25) & (data[features[1]] <= 0.5),       
    }


    mood_labels = mood_mapper(data, mood_map_3D, features)

    return mood_labels












