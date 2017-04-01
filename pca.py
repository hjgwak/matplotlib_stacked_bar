import numpy as np
import matplotlib.pyplot as plt
from extractFeature import load_bacterium
from sklearn.decomposition import PCA

def run(filename, group_filename) :
    
    bacterium = load_bacterium(filename, group_filename)
    X = bacterium['data']
    y = bacterium['group_id']
    group_names = bacterium['group_names']
    sample_names = bacterium['sample']

    # print X,y
    n_components = 2
    
    pca = PCA(n_components=n_components)

    X_pca = pca.fit_transform(X)

    colors = ['navy', 'turquoise', 'darkorange', 'green', 'yellow' ]

    f, ax1 = plt.subplots(1, figsize=(6,6))

    for X_transformed, title in [(X_pca, "PCA")]:
        for color, i, group_name in zip(colors, range(len(group_names)), group_names):
            plt.scatter(X_transformed[y == i, 0], X_transformed[y == i, 1],
                        color=color, lw=2, label=group_name)
            plt.title(title + " of bacterium dataset")
        plt.legend(loc="best", shadow=False, scatterpoints=1)
        plt.axis([-1, 1, -0.5, 0.5])

    for label, x, y in zip(sample_names, X_transformed[:,0], X_transformed[:,1]):
        plt.annotate( label, xy=(x, y), xytext=(-2, 2), textcoords='offset points', ha='right', va='bottom' ,
            fontsize = 6, color = 'gray')

    plt.show()


if __name__ == "__main__":
    filename = './data/Total_CRS_filtered.csv'
    group_filename = './data/group_name.csv'
    run(filename, group_filename)

