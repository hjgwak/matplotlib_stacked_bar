import matplotlib.pyplot as plt
import numpy as np
import readGenus as rg
import stackedSpecies as ss
import matplotlib
from random import random

# Create the general blog and the "subplots" i.e. the bars
f, ax1 = plt.subplots(1, figsize=(12,6))
plt.subplots_adjust(left=0.1, bottom=0.5, right=None, top=0.95,
                    wspace=None, hspace=None)

# Set the bar width
bar_width = 0.35

# positions of the left bar-boundaries
bar_l = [i+1 for i in range(len(rg.x_data))]

bottom_data = [0 for i in range(len(rg.x_data))]

colors = [(1,1,1)] + [(random(),random(),random()) for i in xrange(rg.nrows)]

# Create a bar plot, in position bar_l
for n in range(1, rg.nrows) :
    ax1.bar(bar_l, 
    rg.genus_dic[n]['rate'], 
    width = bar_width, 
    bottom = rg.bottom_data[n-1],
    label = rg.genus_dic[n]['name'],
    color = colors[n], 
    alpha = 0.5)

# set the x ticks with names
plt.xticks(bar_l, rg.x_data, fontsize = 7)

# Set the label and legends
ax1.set_ylabel("Rate(%)")
# ax1.set_xlabel("Table")

plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1),
          fancybox=True, shadow=True, ncol=6, fontsize = 7)


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


def on_plot_hover(event):
    if event.inaxes is not None:
        x, hovered_dic = rg.search_genus(event.xdata, event.ydata, bar_width)
        if x == None :
            print "out of bars"
        else : 
            # print "#",hovered_dic['name'], hovered_dic['type'] , round(hovered_dic['rate'][x],5)
            name = hovered_dic['name']
            ty = hovered_dic['type']
            size = str(round(hovered_dic['rate'][x], 3))
            an = ax1.annotate("genus : "+name+"\ntype:"+ty +"\nsize:"+size+"%", 
                  xy=(event.xdata, event.ydata), xycoords="data",
                  xytext=(event.xdata+0.5, event.ydata), textcoords='data', 
                  va="center", ha="left", bbox=dict(boxstyle="round", fc="w"), 
                  arrowprops=dict(arrowstyle="->", connectionstyle="arc3"))
            an.figure.canvas.draw()
            plt.pause(0.001)
            an.remove()
            
    else:
        print 'Mouse overed ouside axes bounds but inside plot window'
        

f.canvas.mpl_connect('motion_notify_event', on_plot_hover)
f.canvas.callbacks.connect('button_press_event', on_click)

plt.show()
