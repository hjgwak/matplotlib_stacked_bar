import matplotlib.pyplot as plt
from loadData import load_genusData
import stackedSpecies
import matplotlib
# from random import random
from mouseAction import *

def run(genus_filename, species_filename) :
    #set data
    nrows, x_data, genus_dic, bottom_data = load_genusData(genus_filename)
    
    #set data to mouseAction
    set_genusData(genus_filename)
    setSpeciesFile(species_filename)

    # Create the general blog and the "subplots" i.e. the bars
    f, ax1 = plt.subplots(1, figsize=(12,6))
    plt.subplots_adjust(left=0.1, bottom=0.5, right=None, top=0.9,
                        wspace=None, hspace=None)

    # positions of the left bar-boundaries
    bar_l = [i+1 for i in range(len(x_data))]

    # colors = [(0.3+random()*0.6,0.3+random()*0.6,0.3+random()*0.6) for i in xrange(nrows)]

    # Create a bar plot, in position bar_l
    for n in range(1, nrows) :
        gd = genus_dic[n]

        ax1.bar(bar_l, 
        gd['rate'], 
        width = bar_width, 
        bottom = bottom_data[n-1],
        label = gd['name'] +"("+str(gd['type'])[0]+")", #genus(type)
        # color = colors[n-1], 
        alpha = 0.5)

    # set the x ticks with names
    plt.xticks(bar_l, x_data, fontsize = 6, rotation=70)

    # Set the label and legends
    ax1.set_ylabel("Rate(%)")

    plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.2),
              fancybox=True, shadow=True, ncol=6, fontsize = 7)

    cursor = Cursor(ax1)

    plt.connect('motion_notify_event', cursor.mouse_move_genus)
    f.canvas.callbacks.connect('button_press_event', on_click)

    plt.show()

if __name__ == "__main__":
    genus_filename = './data/Total_CRS_filtered.csv'  
    species_filename = '.data/Total_CRS_species.csv'
    run(genus_filename, species_filename)
