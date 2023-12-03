"""
script : tests.py 
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











def get_invalid_indicies(data, custom_function):
    """ 
    Get the indices which doesn't satisfy conditions and raises value error.

    :param data: object - data
    :custom_function: object - function to be checked
    :return: object - list of observation indices

    Description:


    
    """

    error_indices = []
    for idx, row in data.iterrows():
        try:
            custom_function(row)
        except ValueError:
            error_indices.append(idx)

    print(f"Indices causing ValueError: {error_indices}")

    return error_indices





