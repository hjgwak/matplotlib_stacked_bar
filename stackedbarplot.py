import matplotlib.pyplot as plt
import numpy as np
import readGenus as rg

# Create the general blog and the "subplots" i.e. the bars
f, ax1 = plt.subplots(1, figsize=(13,5))

# Set the bar width
bar_width = 0.35

# positions of the left bar-boundaries
bar_l = [i+1 for i in range(len(rg.x_data))]

colors = ['#F4561D', '#F1911E','#F1BD1A', 'yellow']

bottom_data = [0 for i in range(len(rg.x_data))]

# Create a bar plot, in position bar_1
for n in range(len(rg.genus_dic['Acinetobacter'])) :
        keys = rg.genus_dic['Acinetobacter'].keys()

        ax1.bar(bar_l, 
        rg.genus_dic['Acinetobacter'][keys[n]], 
        width = bar_width, 
        bottom = bottom_data,
        label = keys[n], 
        alpha = 0.5, 
        color = colors[n])
        
        bottom_data  = [i+j for i,j in zip(bottom_data, rg.genus_dic['Acinetobacter'][keys[n]])]


# set the x ticks with names
plt.xticks(bar_l, rg.x_data, fontsize = 7)

# Set the label and legends
ax1.set_ylabel("Total Score")
ax1.set_xlabel("Acinetobacter")
plt.legend(loc='upper right')

plt.show()



