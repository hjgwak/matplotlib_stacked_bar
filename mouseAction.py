import searchGenusSpecies as sgs
from loadData import *
import matplotlib.pyplot as plt
import stackedSpecies

# Set the bar width
bar_width = 0.35

#set data
def set_genusData(gfilename) :
    global genus_dic
    global g_bottom_data
    global nrows
    global x_data

    nrows, x_data, genus_dic, g_bottom_data = load_genusData(gfilename)


#set data
def set_speciesData(sfilename, gfilename) :
    global species_dic
    global s_bottom_data
    global nrows
    global x_data

    nrows, x_data, species_dic, s_bottom_data = load_speciesData(sfilename, gfilename)


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
        x, clicked_dic = sgs.search(event.xdata, event.ydata, bar_width, genus_dic, g_bottom_data)
        if x == None :
            print "out of bars"
        else :
            if clicked_dic['type'] == 'genus' :
                stackedSpecies.run(clicked_dic['name'], species_filename, genus_filename)
            else :
                print clicked_dic['type'] ,"can be splited by species"
    else:
        print 'Clicked ouside axes bounds but inside plot window'

class Cursor(object):
    
    def __init__(self, ax):
        self.ax = ax  
        # text location in axes coords
        self.txt = ax.text(0.9, 1.06, '', fontsize = 7, transform=ax.transAxes, bbox={'facecolor':'lightgray', 'pad':8})
        

    def mouse_move_genus(self, event):
        if event.inaxes is not None:
            x, hovered_dic = sgs.search(event.xdata, event.ydata, bar_width, genus_dic, g_bottom_data)
            if x == None :
                self.txt.set_text('out of bars')
            else : 
                name = hovered_dic['name']
                ty = hovered_dic['type']
                size = hovered_dic['rate'][x]
                self.txt.set_text('name=%s\ntype=%s\nsize=%1.3f' % (name, ty, size))
        else:
            self.txt.set_text('ouside axes bounds')

        plt.draw()


    def mouse_move_species(self, event):
        if event.inaxes is not None:
            x, hovered_dic = sgs.search(event.xdata, event.ydata, bar_width, species_dic[genus], s_bottom_data[genus])
            if x == None :
                self.txt.set_text('out of bars')
            else : 
                name = hovered_dic['name']
                size = hovered_dic['rate'][x]
                self.txt.set_text('name=%s\nsize=%1.3f' % (name, size))

        else:
            self.txt.set_text('ouside axes bounds')
        plt.draw()
