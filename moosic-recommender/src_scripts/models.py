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


    print(f"Successful installation of the required dependencies necessary")







# functions
# -- dimensionality reduction (tsne, umap, pca)
# -- clustering models (kmeans, minibatch kmeans, kmode, minibatch kmode, kmeans + kmode, mean shift, dbscan)
# -- text vectorization and similarity computation (tdidf vectorizer, cosine similarity, linear kernel)
# -- classification models (xgboost, svm, logistic regression, naive bayes, random forest)






def clustering_models(dataset, model='kmeans', n_clusters=2, *args, **kwargs):

    """
    Clustering models

    """


    models = {
        'kmeans': KMeans(n_clusters),
        'minibatch_kmeans': MiniBatchKMeans(n_clusters),
        'kmode': KModes(n_clusters),
        'kprototypes': KPrototypes(n_clusters),
        'mean_shift': MeanShift(),
        'dbscan': DBSCAN()
    }

    if model in models:
        clustering_model = models[model]
        return clustering_model.fit_predict(dataset)
    else:
        raise ValueError(f"The clustering model : '{model}' model is currently not available.")


def text_processing(dataset, vectorizer='tfidf', *args, **kwargs):

    """
    Similarity matrix computation - Text vectorization

    """

    vectorizers = {
        'tfidf': lambda d: TfidfVectorizer().fit_transform(d),
        'cosine_similarity': lambda d: cosine_similarity(d),
        'linear_kernel': lambda d: linear_kernel(d)
    }

    if vectorizer in vectorizers:
        text_vectorizer = vectorizers[vectorizer]
        return text_vectorizer(dataset)
    else:
        raise ValueError(f"The text vectorization method : '{vectorizer}' is currently not available.")




def classification_models(dataset, labels, model='xgboost', random_state=42, *args, **kwargs):

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
        return classification_model.fit(dataset, labels)
    else:
        raise ValueError(f"The classification model: '{model}' model is currently not listed.")





def content_recommender(dataset, *args, **kwargs):

    """"
    mood based music content recommendation model
    
    """

    # TBA

    pass

















