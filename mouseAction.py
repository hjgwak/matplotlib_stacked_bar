import searchGenusSpecies as sgs
from loadData import *
import matplotlib.pyplot as plt
import stackedSpecies

# Set the bar width
bar_width = 0.35

#set data
def set_genusData(filename) :
    global genus_dic
    global bottom_data
    global nrows
    global x_data

    nrows, x_data, genus_dic, bottom_data = load_genusData(filename)


#set data
def set_speciesData(filename, gfilename) :
    global species_dic
    global bottom_data
    global nrows
    global x_data

    nrows, x_data, species_dic, bottom_data = load_speciesData(filename, gfilename)


def setFileName(sfilename, gfilename) :
    global species_filename, genus_filename 
    species_filename = sfilename 
    genus_filename = gfilename

#set global genus
def setGenus(genus_name) :
    global genus 
    genus =  genus_name

def on_click(event):
    if event.inaxes is not None:
        # print event.xdata, event.ydata
        x, clicked_dic = sgs.search(event.xdata, event.ydata, bar_width, genus_dic, bottom_data)
        if x == None :
            print "out of bars"
        else :
            if clicked_dic['type'] == 'genus' :
                stackedSpecies.run(clicked_dic['name'], species_filename, genus_filename)
            else :
                print clicked_dic['type'] ,"can be splited by species"
    else:
        print 'Clicked ouside axes bounds but inside plot window'

# class Click(object) :
#     sample_names  = []
#     X_pca = []
    
#     # def __init__(self, ax):
#     #     self.ax = ax  

#     def pca_show(self, event):
#         for label, x, y in zip(self.sample_names, self.X_pca[:,0], self.X_pca[:,1]):
#             plt.annotate( label, xy=(x, y), xytext=(-2, 2), textcoords='offset points',
#                 ha='right', va='bottom', fontsize = 6, color = 'gray')

#         plt.draw()

class Cursor(object):
    
    def __init__(self, ax):
        self.ax = ax  
        # text location in axes coords
        self.txt = ax.text(0.9, 1.06, '', fontsize = 7, transform=ax.transAxes, bbox={'facecolor':'lightgray', 'pad':8})
        

    def mouse_move_genus(self, event):
        if event.inaxes is not None:
            x, hovered_dic = sgs.search(event.xdata, event.ydata, bar_width, genus_dic, bottom_data)
            if x == None :
                self.txt.set_text('out of bars')
                # print "out of bars"
            else : 
                # print "#",hovered_dic['name'], hovered_dic['type'] , round(hovered_dic['rate'][x],5)
                name = hovered_dic['name']
                ty = hovered_dic['type']
                size = hovered_dic['rate'][x]
                self.txt.set_text('name=%s\ntype=%s\nsize=%1.3f' % (name, ty, size))
                # plt.draw()

        else:
            self.txt.set_text('ouside axes bounds')
            # print 'Mouse overed ouside axes bounds but inside plot window'

        plt.draw()


    def mouse_move_species(self, event):
        if event.inaxes is not None:
            x, hovered_dic = sgs.search(event.xdata, event.ydata, bar_width, species_dic[genus], bottom_data[genus])
            if x == None :
                self.txt.set_text('out of bars')
                # print "out of bars"
            else : 
                # print "#",hovered_dic['name'], hovered_dic['type'] , round(hovered_dic['rate'][x],5)
                name = hovered_dic['name']
                size = hovered_dic['rate'][x]
                self.txt.set_text('name=%s\nsize=%1.3f' % (name, size))
                # plt.draw()

        else:
            self.txt.set_text('ouside axes bounds')
            # print 'Mouse overed ouside axes bounds but inside plot window'
        plt.draw()




