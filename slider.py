from matplotlib.colors import LinearSegmentedColormap
import colorsys
import numpy as np

#Create random HSV colors
randHSVcolors = [(np.random.rand(),1,1) for i in xrange(10)]

# Convert HSV list to RGB
randRGBcolors=[]
for HSVcolor in randHSVcolors:
  randRGBcolors.append(colorsys.hsv_to_rgb(HSVcolor[0],HSVcolor[1],HSVcolor[2]))

random_colormap = LinearSegmentedColormap.from_list('new_map', randRGBcolors, N=10)
