from matplotlib import pyplot as plt
import matplotlib.lines as mlines

class draw_graph(object):
	"""docstring for draw_graph"""
	group1 = []
	group2 = []
	x_label = []
	y_label = []
	pvalue_label = []
	fit_data = []
	genus_data = []
	title = []
	x = []

	checked = []

	def __init__(self, group1, group2, checked):
		super(draw_graph, self).__init__()
		self.group1 = group1
		self.group2 = group2
		self.checked = checked

	def draw(self) :
		f, ax1 = plt.subplots(1)
		# f, ax1 = plt.subplots(1, figsize=(14,6), dpi=80)
		plt.subplots_adjust(left=0.2, bottom=None, right=0.9, top=None,
		                    wspace=None, hspace=None)

		im = ax1.imshow(self.fit_data, cmap=plt.cm.Blues)
		ax1.set_aspect('auto')
		plt.colorbar(im, orientation='horizontal')

		plt.title(self.title)
		
		ax1.set_xticks(self.x_label)
		ax1.set_xticklabels(self.group1+self.group2, fontsize=7, rotation=70)
		
		#set label color
		colors = []
		for n in self.x_label :
			if self.x[n] < len(self.group1) :
				colors.append('black')
			else:
				colors.append('red')
		
		#set the axis label color
		for color,tick in zip(colors,ax1.xaxis.get_major_ticks()):
			tick.label1.set_color(color) 

		#y axis on left
		ax1.set_yticks(self.y_label, minor=False)
		ax1.set_yticklabels(self.genus_data, fontsize = 7, minor=False)
		ax1.tick_params(labelbottom='on',labeltop='off', labelleft="on", 
    		top='off', left='off', right='off')
		
		# fig = plt.gcf()
		# size = fig.get_size_inches()*fig.dpi
		# print size
		#y axis on right
		ax2 = f.add_axes(ax1.get_position(), frameon=False)
		ax2.set_yticks(self.y_label, minor=False)
		ax2.set_ylim(ax1.get_ylim())
		ax2.set_yticklabels(self.pvalue_label, fontsize = 7, minor=False)
		ax2.tick_params(labelbottom='off',labeltop='off', labelleft="off", labelright='on',
    			bottom='off', left='off', right='off')

		#set legend
		black_line = mlines.Line2D([], [], color='black',label=self.checked[0])
		red_line = mlines.Line2D([], [], color='red',label=self.checked[1])
		plt.legend(handles=[black_line, red_line],loc='lower right', bbox_to_anchor=(1., 1.), fontsize =7)

