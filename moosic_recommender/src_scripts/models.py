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


    # high dimensional usage - dimensionality reduction
    from sklearn.manifold import TSNE
    from sklearn.decomposition import PCA
    from umap import UMAP

    # modelling - clustering
    from sklearn.cluster import KMeans, MiniBatchKMeans, MeanShift, DBSCAN
    from kmodes.kmodes import KModes
    from kmodes.kprototypes import KPrototypes

    # text processing - vectorizer - similarity computation
    from sklearn.feature_extraction.text  import TfidfVectorizer
    from sklearn.metrics.pairwise import linear_kernel,sigmoid_kernel, cosine_similarity


    # modelling - classification
    import xgboost as xgb
    from xgboost import XGBClassifier
    from sklearn.svm import SVC
    from sklearn.linear_model import LogisticRegression
    from sklearn.naive_bayes import GaussianNB, MultinomialNB
    from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, GradientBoostingClassifier

    # transformers - attention model
    from transformers import BertTokenizer, BertModel, BertForTokenClassification

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
    subprocess.check_call(["pip", "install", "kmodes"])
    subprocess.check_call(["pip", "install", "kprototypes"])
    subprocess.check_call(["pip", "install", "transformers"])



    print(f"Successful installation of the required dependencies necessary")


# monitoring and logging with mlflow
import mlflow
import warnings
warnings.filterwarnings('ignore')


# custom imports

from .data_processing import (
        data_preprocessor, 
        dimensionality_reduction, 
        cross_validation,
        )


from .config import (
        EXPERIMENT_NAME,
        )
TRACKING_URI = open("../.mlflow_uri").read().strip()




# functions
# -- dimensionality reduction (tsne, umap, pca)
# -- clustering models (kmeans, minibatch kmeans, kmode, minibatch kmode, kmeans + kmode, mean shift, dbscan)
# -- text vectorization and similarity computation (tdidf vectorizer, cosine similarity, linear kernel)
# -- classification models (xgboost, svm, logistic regression, naive bayes, random forest)




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
        #return reduction_method.fit_transform(data)
        return reduction_method
    
    else:
        raise ValueError(f"The dimensionality reduction technique: '{method}' is currently not available.")





def clustering_models(data, model='kmeans', n_clusters=2, random_state=42, *args, **kwargs):

    """
    Clustering models

    """


    models = {
        'kmeans': KMeans(n_clusters, random_state=random_state),
        'minibatch_kmeans': MiniBatchKMeans(n_clusters, random_state=random_state),
        'kmode': KModes(n_clusters),
        'kprototypes': KPrototypes(n_clusters),
        'mean_shift': MeanShift(),
        'dbscan': DBSCAN()
    }

    if model in models:
        clustering_model = models[model]
        #return clustering_model.fit_predict(data)
        return clustering_model

    else:
        raise ValueError(f"The clustering model : '{model}' model is currently not available.")



def text_vectorization(data, vectorizer='tfidf', *args, **kwargs):

    """
    Similarity matrix computation - Text vectorization

    """

    # vectorizers = {
    #     'tfidf': lambda d: TfidfVectorizer().fit_transform(d),
    #     'cosine_similarity': lambda d: cosine_similarity(d),
    #     'linear_kernel': lambda d: linear_kernel(d)
    # }

    vectorizers = {
        'tfidf': lambda d: TfidfVectorizer().fit_transform(d),
        'cosine_similarity': lambda d: cosine_similarity(d),
        'linear_kernel': lambda d: linear_kernel(d)
    }

    if vectorizer in vectorizers:
        text_vectorizer = vectorizers[vectorizer]
        return text_vectorizer(data)
    else:
        raise ValueError(f"The text vectorization method : '{vectorizer}' is currently not available.")




def model_pipeline(data):

    """"
    model pipeline for training
        - dimensionality reduction
        - clustering
        - vectorization and similarity computation
        - save model : object serialization
        - save similarity matrix  : object serialization
    
    
    """

    pipeline = Pipeline([
        ('dim_embed', TSNE(n_components=2)),
        ('cluster_model', MiniBatchKMeans(n_clusters=5, random_state=42)),
    ])


    results = pipeline.fit_transform(data)

    return results





def content_vectorization_similarity(data, user_query):

    """"
    converting data to numerical rrepresentations
    computing similarities

    """

    pass




def content_recommender(data, user_query, track_feature_matrix, track_id_to_index, playlist_lenght=5, *args, **kwargs):

    """"
    mood based music content recommendater
        search engine for querying users request

    """


    
    pass 





def classification_models(data, labels, model='xgboost', random_state=42, *args, **kwargs):

    """
    Classification models

    """

    models = {
        'xgboost': XGBClassifier(random_state=random_state),
        'svm': SVC(random_state=random_state),
        'logistic_regression': LogisticRegression(random_state=random_state),
        'gaussian_naive_bayes': GaussianNB(),
        'multinomial_naive_bayes': MultinomialNB(),
        'random_forest': RandomForestClassifier(random_state=random_state),
        'adaboost': AdaBoostClassifier(random_state=random_state),
        'gradientboost': GradientBoostingClassifier(random_state=random_state)
    }

    if model in models:
        classification_model = models[model]
        return classification_model.fit(data, labels)
    else:
        raise ValueError(f"The classification model: '{model}' model is currently not listed.")













