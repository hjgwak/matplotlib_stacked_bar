import matplotlib.pyplot as plt
import readSpecies as rs
import matplotlib
from random import random
import searchGenusSpecies as sgs

# Set the bar width
bar_width = 0.35

#set global genus
def setGenus(genus_name) :
    global genus 
    genus =  genus_name

class Cursor(object):
    def __init__(self, ax):
        self.ax = ax  
        # text location in axes coords
        self.txt = ax.text(0.9, -0.25, '', fontsize = 7, transform=ax.transAxes, bbox={'facecolor':'lightgray', 'pad':8})

    def mouse_move(self, event):
        if event.inaxes is not None:
            x, hovered_dic = sgs.search(event.xdata, event.ydata, bar_width, rs.species_dic[genus], rs.bottom_data[genus])
            if x == None :
                print "out of bars"
            else : 
                # print "#",hovered_dic['name'], hovered_dic['type'] , round(hovered_dic['rate'][x],5)
                name = hovered_dic['name']
                size = hovered_dic['rate'][x]
                self.txt.set_text('name=%s\nsize=%1.3f' % (name, size))
                plt.draw()

        else:
            print 'Mouse overed ouside axes bounds but inside plot window'

def run(genus) :
    
    setGenus(genus)

    # Create the general blog and the "subplots" i.e. the bars
    f, ax1 = plt.subplots(1, figsize=(12,5))
    plt.subplots_adjust(left=0.1, bottom=0.4, right=None, top=0.9,
                wspace=None, hspace=None)


    # positions of the left bar-boundaries
    bar_l = [i+1 for i in range(len(rs.x_data))]

    bottom_data = [0 for i in range(len(rs.x_data))]
    
    colors = [(0.3+random()*0.6,0.3+random()*0.6,0.3+random()*0.6) for i in xrange(rs.nrows)]

    # Create a bar plot, in position bar_l
    for n in range(1, len(rs.species_dic[genus])+1) :

        ax1.bar(bar_l, 
            rs.species_dic[genus][n]['rate'], 
            width = bar_width, 
            bottom = rs.bottom_data[genus][n-1],
            label = rs.species_dic[genus][n]['name'], 
            color = colors[n-1],
            alpha = 0.8)

    # set the x ticks with names
    plt.xticks(bar_l, rs.x_data, fontsize = 7)

    # Set the label and legends
    ax1.set_ylabel("Rate")
    ax1.set_xlabel(genus)
    plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.3),
      fancybox=True, shadow=True, ncol=5, fontsize = 8)

    cursor = Cursor(ax1)
    plt.connect('motion_notify_event', cursor.mouse_move)
    plt.show()

if __name__ == "__main__":
        genus_name = 'Methylobacterium'
        setGenus(genus_name)
        run(genus_name)

