import matplotlib.pyplot as plt
import numpy as np
import readGenus as rg
import stackedbarplot as sbp



def on_click(event):
    if event.inaxes is not None:
        print event.xdata, event.ydata
        sbp.run('Acinetobacter')
    else:
        print 'Clicked ouside axes bounds but inside plot window'


# Create the general blog and the "subplots" i.e. the bars
f, ax1 = plt.subplots(1, figsize=(12,5))
plt.subplots_adjust(left=0.1, bottom=0.65, right=None, top=0.95,
                    wspace=None, hspace=None)

# Set the bar width
bar_width = 0.35

# positions of the left bar-boundaries
bar_l = [i+1 for i in range(len(rg.x_data))]

bottom_data = [0 for i in range(len(rg.x_data))]

# Create a bar plot, in position bar_l
for n in range(len(rg.genus_dic.keys())) :
        keys = rg.genus_dic.keys()

        ax1.bar(bar_l, 
        rg.genus_dic[keys[n]]['rate'], 
        width = bar_width, 
        bottom = bottom_data,
        label = keys[n], 
        alpha = 0.5)

        bottom_data  = [i+j for i,j in zip(bottom_data, rg.genus_dic[keys[n]]['rate'])]


# set the x ticks with names
plt.xticks(bar_l, rg.x_data, fontsize = 7)

# Set the label and legends
ax1.set_ylabel("Rate")
# ax1.set_xlabel("Table")
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.3),
          fancybox=True, shadow=True, ncol=6, fontsize = 7)
# plt.legend(loc='right', bbox_to_anchor=(1, 0.5))

f.canvas.callbacks.connect('button_press_event', on_click)

plt.show()
