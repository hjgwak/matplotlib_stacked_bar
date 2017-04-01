import numpy as np
import matplotlib.pyplot as plt
from extractFeature import load_bacterium
from sklearn.decomposition import PCA

def run(filename, group_filename) :
    bacterium = load_bacterium(filename, group_filename)
    X = bacterium['data']
    y = bacterium['target']
    target_names = bacterium['target_names']

    pca = PCA(n_components=len(target_names))
    X_pca = pca.fit_transform(X)

    colors = ['navy', 'turquoise', 'darkorange', 'green' ]

    for X_transformed, title in [(X_pca, "PCA")]:
        plt.figure(figsize=(6, 6))
        for color, i, target_name in zip(colors, range(len(target_names)), target_names):
            plt.scatter(X_transformed[y == i, 0], X_transformed[y == i, 1],
                        color=color, lw=2, label=target_name)
            plt.title(title + " of bacterium dataset")
        plt.legend(loc="best", shadow=False, scatterpoints=1)
        plt.axis([-1, 1, -0.5, 0.5])

    plt.show()

if __name__ == "__main__":
    filename = './data/Total_CRS_filtered.csv'
    group_filename = './data/group_name.csv'
    run(filename, group_filename)

