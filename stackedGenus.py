import matplotlib.pyplot as plt
import numpy as np
import readGenus as rg
import stackedSpecies as ss
import matplotlib
from random import random

class Cursor(object):
    def __init__(self, ax):
        self.ax = ax  
        # text location in axes coords
        self.txt = ax.text(1.0, 0.0, '', fontsize = 7, transform=ax.transAxes, bbox={'facecolor':'lightgray', 'pad':8})

    def mouse_move(self, event):
        if event.inaxes is not None:
            x, hovered_dic = rg.search_genus(event.xdata, event.ydata, bar_width)
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
        x, clicked_dic = rg.search_genus(event.xdata, event.ydata, bar_width)
        if x == None :
            print "out of bars"
        else :
            if clicked_dic['type'] == 'genus' :
                ss.run(clicked_dic['name'])
            else :
                print clicked_dic['type'] ,"can be splited by species"
    else:
        print 'Clicked ouside axes bounds but inside plot window'


# Create the general blog and the "subplots" i.e. the bars
f, ax1 = plt.subplots(1, figsize=(12,6))
plt.subplots_adjust(left=0.1, bottom=0.5, right=None, top=0.95,
                    wspace=None, hspace=None)

# Set the bar width
bar_width = 0.35

# positions of the left bar-boundaries
bar_l = [i+1 for i in range(len(rg.x_data))]

bottom_data = [0 for i in range(len(rg.x_data))]

colors = [(0.3+random()*0.6,0.3+random()*0.6,0.3+random()*0.6) for i in xrange(rg.nrows)]

# Create a bar plot, in position bar_l
for n in range(1, rg.nrows) :
    gd = rg.genus_dic[n]

    ax1.bar(bar_l, 
    gd['rate'], 
    width = bar_width, 
    bottom = rg.bottom_data[n-1],
    label = gd['name'] +"("+str(gd['type'])[0]+")",
    color = colors[n-1], 
    alpha = 0.8)

# set the x ticks with names
plt.xticks(bar_l, rg.x_data, fontsize = 7)

# Set the label and legends
ax1.set_ylabel("Rate(%)")

plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1),
          fancybox=True, shadow=True, ncol=6, fontsize = 7)

cursor = Cursor(ax1)

plt.connect('motion_notify_event', cursor.mouse_move)
f.canvas.callbacks.connect('button_press_event', on_click)

plt.show()
