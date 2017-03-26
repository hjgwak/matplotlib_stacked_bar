import matplotlib.pyplot as plt
from readGenus import loadData
import stackedSpecies
import matplotlib
from random import random
import searchGenusSpecies as sgs

# Set the bar width
bar_width = 0.35

def setSpeciesFile(filename) :
    global species_filename 
    species_filename =  filename


#set data
def setData(filename) :
    global genus_dic
    global bottom_data
    global nrows
    global x_data

    nrows, x_data, genus_dic, bottom_data = loadData(filename)


class Cursor(object):
    def __init__(self, ax):
        self.ax = ax  
        # text location in axes coords
        self.txt = ax.text(1.0, 0.0, '', fontsize = 7, transform=ax.transAxes, bbox={'facecolor':'lightgray', 'pad':8})

    def mouse_move(self, event):
        if event.inaxes is not None:
            x, hovered_dic = sgs.search(event.xdata, event.ydata, bar_width, genus_dic, bottom_data)
            if x == None :
                print "out of bars"
            else : 
                # print "#",hovered_dic['name'], hovered_dic['type'] , round(hovered_dic['rate'][x],5)
                name = hovered_dic['name']
                ty = hovered_dic['type']
                size = hovered_dic['rate'][x]
                self.txt.set_text('name=%s\ntype=%s\nsize=%1.3f' % (name, ty, size))
                plt.draw()

        else:
            print 'Mouse overed ouside axes bounds but inside plot window'


def on_click(event):
    if event.inaxes is not None:
        # print event.xdata, event.ydata
        x, clicked_dic = sgs.search(event.xdata, event.ydata, bar_width, genus_dic, bottom_data)
        if x == None :
            print "out of bars"
        else :
            if clicked_dic['type'] == 'genus' :
                stackedSpecies.run(clicked_dic['name'], species_filename)
            else :
                print clicked_dic['type'] ,"can be splited by species"
    else:
        print 'Clicked ouside axes bounds but inside plot window'


def run(genus_filename, species_filename) :
    setData(genus_filename)
    setSpeciesFile(species_filename)

    # Create the general blog and the "subplots" i.e. the bars
    f, ax1 = plt.subplots(1, figsize=(12,6))
    plt.subplots_adjust(left=0.1, bottom=0.5, right=None, top=0.95,
                        wspace=None, hspace=None)

    # positions of the left bar-boundaries
    bar_l = [i+1 for i in range(len(x_data))]

    colors = [(0.3+random()*0.6,0.3+random()*0.6,0.3+random()*0.6) for i in xrange(nrows)]

    # Create a bar plot, in position bar_l
    for n in range(1, nrows) :
        gd = genus_dic[n]

        ax1.bar(bar_l, 
        gd['rate'], 
        width = bar_width, 
        bottom = bottom_data[n-1],
        label = gd['name'] +"("+str(gd['type'])[0]+")", #genus(type)
        color = colors[n-1], 
        alpha = 0.8)

    # set the x ticks with names
    plt.xticks(bar_l, x_data, fontsize = 7)

    # Set the label and legends
    ax1.set_ylabel("Rate(%)")

    plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1),
              fancybox=True, shadow=True, ncol=6, fontsize = 7)

    cursor = Cursor(ax1)

    plt.connect('motion_notify_event', cursor.mouse_move)
    f.canvas.callbacks.connect('button_press_event', on_click)

    plt.show()

if __name__ == "__main__":
    genus_filename = 'CRS_above_genus.csv'  
    species_filename = 'CRS_genus_species.csv'
    run(genus_filename, species_filename)
