
"""
script : main.py 
purpose: main file 


"""



# Importing necessary libraries and modules for modelling

import subprocess

try:

    import numpy as np
    import pandas as pd
    import random as rnd


    # pipeline
    from sklearn.pipeline import Pipeline
    from sklearn.pipeline import make_pipeline


except ImportError as error:
    print(f"Installation of the required dependencies necessary! {error}")

    subprocess.check_call(["pip", "install", "numpy"])
    subprocess.check_call(["pip", "install", "pandas"])
    subprocess.check_call(["pip", "install", "scikit-learn"])
    subprocess.check_call(["pip", "install", "xgboost"])
    subprocess.check_call(["pip", "install", "deap"])
    subprocess.check_call(["pip", "install", "umap-learn"])


    print(f"Successful installation of the required dependencies necessary")





from .data_processing import dimensionality_reduction, data_scaling_normalization, cross_validation
from .models import clustering_models, text_processing, classification_models, content_recommender
from .evaluation_metrics import clustering_metrics, classification_metrics
from .visualizations import optimal_cluster_plot, evaluation_metrics_plots


























