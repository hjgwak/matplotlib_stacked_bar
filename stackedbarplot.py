import matplotlib.pyplot as plt
import numpy as np
import readSpecies as rs

def run(genus) :
        # Create the general blog and the "subplots" i.e. the bars
        f, ax1 = plt.subplots(1, figsize=(12,5))

        # Set the bar width
        bar_width = 0.35

        # positions of the left bar-boundaries
        bar_l = [i+1 for i in range(len(rs.x_data))]

        bottom_data = [0 for i in range(len(rs.x_data))]
        
        # Create a bar plot, in position bar_l
        for n in range(len(rs.species_dic[genus])) :
                keys = rs.species_dic[genus].keys()
                ax1.bar(bar_l, 
                rs.species_dic[genus][keys[n]], 
                width = bar_width, 
                bottom = bottom_data,
                label = keys[n], 
                alpha = 0.5)

                bottom_data  = [i+j for i,j in zip(bottom_data, rs.species_dic[genus][keys[n]])]


        # set the x ticks with names
        plt.xticks(bar_l, rs.x_data, fontsize = 7)

        # Set the label and legends
        ax1.set_ylabel("Rate")
        ax1.set_xlabel(genus)
        plt.legend(loc='best')

        plt.show()

if __name__ == "__main__":
        genus_name = 'Acinetobacter'
        run(genus_name)

