import numpy as np
import matplotlib.pyplot as plt
from extractFeature import load_bacterium
from sklearn.decomposition import PCA
import csvReader

def run(filename, group_filename) :
    csv_list, nrows, ncols = csvReader.csv_reader(filename)
    bacterium = load_bacterium(filename, group_filename)
    X = bacterium['data']
    y = bacterium['group_id']
    group_names = bacterium['group_names']
    
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

    #loadings
    # print len(csv_list)
    # print len(pca.components_[0])
    for i in range(len(pca.components_[0])):
        x, y = pca.components_[0][i], pca.components_[1][i]
        # print x,y
        if x>0.3 or y > 0.3 :
            # print csv_list[i][0]
            plt.arrow(0, 0, x*0.5, y*0.5, color='salmon',
                      width=0.001, head_width=0.01)
            plt.text(x*0.25, y*0.25 , csv_list[i+1][0], color='salmon', ha='center', va='center', fontsize = 7)


    #set annotation
    for label, x, y in zip(bacterium['sample'], X_pca[:,0], X_pca[:,1]):
        plt.annotate( label, xy=(x, y), xytext=(-2, 2), textcoords='offset points',
            ha='right', va='bottom', fontsize = 6, color = 'gray')

    plt.show()


if __name__ == "__main__":
    filename = './data/Total_CRS_filtered.csv'
    group_filename = './data/group_name.csv'
    run(filename, group_filename)

