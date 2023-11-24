# Importing necessary libraries and modules for modelling

import subprocess

try:

    import numpy as np
    import pandas as pd
    import random as rnd

    # metrics
    from sklearn import metrics
    from sklearn.metrics import accuracy_score, roc_auc_score, classification_report, confusion_matrix, roc_curve

    from sklearn.metrics import silhouette_score, calinski_harabasz_score
    from sklearn.metrics import adjusted_rand_score, homogeneity_score, completeness_score, v_measure_score, ndcg_score
    from sklearn.metrics import precision_score, recall_score, f1_score, average_precision_score




except ImportError as error:
    print(f"Installation of the required dependencies necessary! {error}")

    subprocess.check_call(["pip", "install", "numpy"])
    subprocess.check_call(["pip", "install", "pandas"])
    subprocess.check_call(["pip", "install", "scikit-learn"])



    print(f"Successful installation of the required dependencies necessary")


import warnings
warnings.filterwarnings('ignore')





# evaluation metrics : clustering



def clustering_metrics(true_labels, predictions, metric='rand_index', dataset=None, silhouette=True, *args, **kwargs):

    """
    clustering metrics 
        - rand index
        - v_measure
        - silhouette
        - etc
    """

    if silhouette == False:

        evaluation_metrics = {
            'rand_index': lambda gt, yhat: adjusted_rand_score(gt, yhat),
            'homogeneity_score': lambda gt, yhat: homogeneity_score(gt, yhat),
            'completeness_score': lambda gt, yhat: completeness_score(gt, yhat),
            'v_measure': lambda gt, yhat: v_measure_score(gt, yhat),
            'ndcg': lambda gt, yhat: ndcg_score([gt], [yhat]),
            'adjusted_rand_score': lambda gt, yhat: precision_score(gt, yhat),

        }

    else:
        
        evaluation_metrics = {
            'silhouette_score': lambda gt, yhat: silhouette_score(dataset, yhat),
            'calinski_harabasz_score': lambda gt, yhat: calinski_harabasz_score(dataset, yhat),

        }

    if metric in evaluation_metrics:
        evaluation_function = evaluation_metrics[metric]
        return evaluation_function(true_labels.to_numpy(), predictions.to_numpy())
    else:
        raise ValueError(f"The evaluation metric: '{metric}' is not supported.")




def classification_metrics(true_labels, predictions, metric='rand_index'):

    """
    classification metrics 
        - rand index
        - v_measure
        - silhouette
        - etc
    """

    evaluation_metrics = {

        'accuracy_score': lambda gt, yhat: accuracy_score(gt, yhat),
        'roc_curve': lambda gt, yhat: roc_curve(gt, yhat),
        'roc_auc_score': lambda gt, yhat: roc_auc_score(gt, yhat),
        'precision': lambda gt, yhat: precision_score(gt, yhat),
        'recall': lambda gt, yhat: recall_score(gt, yhat),
        'f1_score': lambda gt, yhat: f1_score(gt, yhat),
        'mean_average_precision': lambda gt, yhat: average_precision_score(gt, yhat),
        'confusion_matrix': lambda gt, yhat: confusion_matrix(gt, yhat),
        'classification_report': lambda gt, yhat: classification_report(gt, yhat)

    }

    if metric in evaluation_metrics:
        evaluation_function = evaluation_metrics[metric]
        return evaluation_function(true_labels, predictions)
    else:
        raise ValueError(f"The evaluation metric: '{metric}' is not supported.")


def evaluation_metrics(true_labels, predictions, metric='rmse', dataset=None):

    """
    Other evaluation metrics (regression, etc)
        - mean_absolute_error
        - mean_square_error
        - root_mean_square_error
        - mean_absolute_percentage_error
        - mean_absolute_error

        - etc
    
    """


    evaluation_metrics = {
        'mae': lambda gt, yhat: metrics.mean_absolute_error(gt, yhat),
        'mse': lambda gt, yhat: metrics.mean_square_error(gt, yhat),
        'rsme': lambda gt, yhat: metrics.root_mean_square_error(gt, yhat),
        'mape': lambda gt, yhat: metrics.mean_absolute_percentage_error(gt, yhat),
        'evs': lambda gt, yhat: metrics.explained_variance_score(gt, yhat),

        }

    if metric in evaluation_metrics:
        evaluation_function = evaluation_metrics[metric]
        return evaluation_function(true_labels, predictions)
    else:
        raise ValueError(f"The evaluation metric: '{metric}' is not supported.")











