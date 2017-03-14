import matplotlib.pyplot as plt
import numpy as np
import readGenus as rg
import stackedbarplot as sbp


# Create the general blog and the "subplots" i.e. the bars
f, ax1 = plt.subplots(1, figsize=(12,6))
plt.subplots_adjust(left=0.1, bottom=0.5, right=None, top=0.95,
                    wspace=None, hspace=None)

# Set the bar width
bar_width = 0.35

# positions of the left bar-boundaries
bar_l = [i+1 for i in range(len(rg.x_data))]

bottom_data = [0 for i in range(len(rg.x_data))]

# Create a bar plot, in position bar_l
for n in range(1, rg.nrows) :
    ax1.bar(bar_l, 
    rg.genus_dic[n]['rate'], 
    width = bar_width, 
    bottom = rg.bottom_data[n-1],
    label = rg.genus_dic[n]['name'], 
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
        genus, ty = rg.search_genus(event.xdata, event.ydata, bar_width)
        if ty == 'Genus' :
            sbp.run(genus)
        else :
            print ty ,"can be splited by species"
    else:
        print 'Clicked ouside axes bounds but inside plot window'


def on_plot_hover(event):
    if event.inaxes is not None:
        genus, ty = rg.search_genus(event.xdata, event.ydata, bar_width)
        if genus == None :
            print "out of bars"
        else : 
            print genus, ty
            an = ax1.annotate("genus : "+genus +"\ntype:"+ty, xy=(event.xdata, event.ydata), xycoords="data",
                  xytext=(event.xdata+0.5, event.ydata), textcoords='data', 
                  va="center", ha="left", bbox=dict(boxstyle="round", fc="w"), 
                  arrowprops=dict(arrowstyle="->", connectionstyle="arc3"))
            an.figure.canvas.draw()
            plt.pause(0.5)
            an.remove()
    else:
        print 'Mouse overed ouside axes bounds but inside plot window'


f.canvas.mpl_connect('motion_notify_event', on_plot_hover)
f.canvas.callbacks.connect('button_press_event', on_click)

plt.show()
