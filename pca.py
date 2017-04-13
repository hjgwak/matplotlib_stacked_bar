import matplotlib.pyplot as plt
from extractFeature import load_bacterium
from sklearn.decomposition import PCA
import csvReader

from matplotlib.widgets import Slider, Button

def run(genus_filename, group_filename) :
    #load genus file
    csv_list, nrows, ncols = csvReader.csv_reader(genus_filename)
    
    #load bacterium data
    bacterium = load_bacterium(genus_filename, group_filename)
    X = bacterium['data']
    y = bacterium['group_id']
    group_names = bacterium['group_names']
    
    n_components = 2
    
    pca = PCA(n_components=n_components)
    X_pca = pca.fit_transform(X)

    colors = ['navy', 'turquoise', 'darkorange', 'green', 'yellow' ]

    f, ax1 = plt.subplots(1, figsize=(6,6))
    plt.subplots_adjust(left=None, bottom=0.2, right=None, top=None,
                        wspace=None, hspace=None)

    #draw scatters
    for X_transformed, title in [(X_pca, "PCA")]:
        for color, i, group_name in zip(colors, range(len(group_names)), group_names):
            plt.scatter(X_transformed[y == i, 0], X_transformed[y == i, 1],
                        color=color, lw=2, label=group_name)
            plt.title(title + " of bacterium dataset")
        plt.legend(loc="best", shadow=False, scatterpoints=1)
        plt.axis([-1, 1, -0.5, 0.5])

    global ann
    ann = []

    #set annotation
    def annotation() : 
        for label, x, y in zip(bacterium['sample'], X_pca[:,0], X_pca[:,1]):
            ann.append(ax1.annotate( label, xy=(x, y), xytext=(-2, 2), textcoords='offset points',
                ha='right', va='bottom', fontsize = 6, color = 'gray'))

    global txt, arr
    txt = []
    arr = []

    #loadings
    def loading(load) :
        for i in range(len(pca.components_[0])):
            x, y = pca.components_[0][i], pca.components_[1][i]
            if x> load or y > load :
                arr.append(ax1.arrow(0, 0, x*0.5, y*0.5, color='coral', width=0.001, head_width=0.01))
                txt.append(ax1.text(x*0.25, y*0.25 , csv_list[i+1][0], color='coral', ha='center', va='center', fontsize = 7))
        f.canvas.draw()
        
    axloading  = plt.axes([0.20, 0.10, 0.62, 0.03], axisbg='lightgoldenrodyellow')
    sloading = Slider(axloading, 'loading', 0.05, 0.5, valinit=0.3, color = 'coral')

    def update(val):
        for i in range(len(txt)) :
            txt[i].remove()
            arr[i].remove()
        arr[:] = []
        txt[:] = []
        
        load = sloading.val
        loading(load)
        f.canvas.draw_idle()

    sloading.on_changed(update)
    showax = plt.axes([0.7, 0.025, 0.1, 0.04])
    hideax = plt.axes([0.8, 0.025, 0.1, 0.04])
    
    bshow = Button(showax, 'show', color='lightgoldenrodyellow', hovercolor='0.975')
    bhide = Button(hideax, 'hide', color='lightgoldenrodyellow', hovercolor='0.975')
    
    def show(event) :
        annotation()

    def hide(event):
        for i in range(len(txt)) :
            txt[i].remove()
            arr[i].remove()
        arr[:] = []
        txt[:] = []
       
        for i in range(len(ann)) :
            ann[i].remove()
        ann[:] = []

        f.canvas.draw()
        
    bshow.on_clicked(show)
    bhide.on_clicked(hide)
  
    plt.show()


if __name__ == "__main__":
    genus_filename = './data/Total_CRS_filtered.csv'
    group_filename = './data/group_name.csv'
    run(genus_filename, group_filename)

