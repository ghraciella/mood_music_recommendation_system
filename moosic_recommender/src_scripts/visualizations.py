
"""
script : visualizations.py 
purpose: visualizations - plots .. 


"""



# Importing necessary libraries and modules for visualization

import subprocess

try:

    import numpy as np
    import pandas as pd
    import random as rnd

    # visualisation
    import seaborn as sns
    import matplotlib.pyplot as plt
    from matplotlib.colors import ListedColormap

    # others
    from sklearn import metrics
    from sklearn.manifold import TSNE
    from sklearn.cluster import MiniBatchKMeans
    from umap import UMAP

except ImportError as error:
    print(f"Installation of the required dependencies necessary! {error}")

    subprocess.check_call(["pip", "install", "numpy"])
    subprocess.check_call(["pip", "install", "pandas"])
    subprocess.check_call(["pip", "install", "scikit-learn"])
    subprocess.check_call(["pip", "install", "matplotlib"])
    subprocess.check_call(["pip", "install", "umap-learn"])


    print(f"Successful installation of the required dependencies necessary")








def hypothesis_testing():

    pass


def eda_():

    pass




def optimal_cluster_plot(data, tsne=True, *args, **kwargs):

    wcss_inertias = []

    if tsne == True:
        tsne = TSNE(n_components=2)
        data = tsne.fit_transform(data)

    else:
        data = data

    for k in range(4, 20):
        model = MiniBatchKMeans(n_clusters=k)
        model.fit(data)
        wcss_inertias.append(model.inertia_)
        
    fig, ax = plt.subplots(nrows=1, ncols=1)
    ax.plot(range(4, 20), wcss_inertias, '-o')
    plt.xlabel('Number of clusters')
    plt.ylabel('WCSS : Within clusters sum of squares')
    plt.title('Elbow method to determine optimal K number of clusters')
    plt.xticks(range(4, 20))
    plt.show(); 





def evaluation_metrics_plots(true_labels, predictions, metric='cm_plot', *args, **kwargs):

    """
    plots of evaluation metrics
        - cm_plot: ConfusionMatrixDisplay
        - rocc_plot: RocCurveDisplay
        - det_plot: DetCurveDisplay
        - pr_plot: PrecisionRecallDisplay
        - etc
    
    """

    display_metrics = {
        'cm_plot': metrics.ConfusionMatrixDisplay,
        'rocc_plot': metrics.RocCurveDisplay,
        'pr_plot': metrics.PrecisionRecallDisplay,
        'det_plot': metrics.DetCurveDisplay,
        'pe_plot': metrics.PredictionErrorDisplay,
        'cal_plot': metrics.CalibrationDisplay,
    }

    if metric in display_metrics:
        metric_plot = display_metrics[metric](true_labels, predictions)
        metric_plot.plot()
        plt.title(metric)
        plt.show()
    else:
        raise ValueError(f"The evaluation metric: '{metric}' is not supported.")






















