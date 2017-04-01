import matplotlib.pyplot as plt
from loadData import load_speciesData
import matplotlib
# from random import random
from mouseAction import *

def run(genus, filename) :
    
    #set data
    nrows, x_data, species_dic, bottom_data = load_speciesData(filename)

    #set data to mouseAction
    setGenus(genus)
    set_speciesData(filename)
    # Create the general blog and the "subplots" i.e. the bars
    f, ax1 = plt.subplots(1, figsize=(12,6))
    plt.subplots_adjust(left=0.1, bottom=0.4, right=None, top=0.9,
                wspace=None, hspace=None)


    # positions of the left bar-boundaries
    bar_l = [i+1 for i in range(len(x_data))]
 
    # colors = [(0.3+random()*0.6,0.3+random()*0.6,0.3+random()*0.6) for i in xrange(nrows)]

    # Create a bar plot, in position bar_l
    for n in range(1, len(species_dic[genus])+1) :

        ax1.bar(bar_l, 
            species_dic[genus][n]['rate'], 
            width = bar_width, 
            bottom = bottom_data[genus][n-1],
            label = species_dic[genus][n]['name'], 
            # color = colors[n-1],
            alpha = 0.5)

    # set the x ticks with names
    plt.xticks(bar_l, x_data, fontsize = 6, rotation=70)

    # Set the label and legends
    ax1.set_ylabel("Rate")
    ax1.set_xlabel(genus)
    plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.4),
      fancybox=True, shadow=True, ncol=5, fontsize = 8)

    cursor = Cursor(ax1)
    plt.connect('motion_notify_event', cursor.mouse_move_species)
    plt.show()

if __name__ == "__main__":
    genus_name = 'Moraxella'
    filename = './data/Total_CRS_species.csv'
    run(genus_name, filename)

