
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



# custom imports


from .dataloader import (
        get_sql_config,
        get_data_structured_file,
        get_data_serialized_file,
        get_data_postgres_db,
        get_conn_engine_alchemy, 
        )


from .data_processing import (
        data_preprocessor, 
        dimensionality_reduction, 
        cross_validation,
        )
from .models import (
        clustering_models, 
        text_processing, 
        classification_models, 
        content_recommender,
        )
from .evaluation_metrics import ( 
        clustering_metrics, 
        classification_metrics,
        )
from .visualizations import  (
        optimal_cluster_plot, 
        evaluation_metrics_plots,
        )



def main():

    # load data

    # data wrangling and processing


    # model 
    # dimensionality reduction
    # clustering
    # similarity computation
    # recommendation engine

    # classification for user-item data 


    """

    main file to build recommendation

    moosic data pipeline
        - extract and load data
        - data_transformations : wrangling
        - target feature engineering : mood and genre
        - avoiding data leakage : train-test-split data
        - getting balanced data
        - data scaling and preprocessing : normalisation of numerical data, encoding of categorical data
        - column transformers
        - save data as embeddings

    cross validation and hyperparameter tuning
        - 



    model pipeline for training
        - dimensionality reduction
        - clustering
        - vectorization and similarity computation
        - save model : object serialization
        - save similarity matrix  : object serialization
        
    
    evaluation metrics and logging
        - clustering metrics
        - mlflow logging and monitoring
        - visualizations

    recommendation
        - get query : user preferences
        - load saved trained model 
        - load similarity matrix 
        - query engine: get similar items indices based on playlist_length
        - recomendation and predictions






    """







    pass 

















