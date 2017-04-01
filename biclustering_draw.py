from matplotlib import pyplot as plt
import matplotlib.lines as mlines

class draw_graph(object):
	"""docstring for draw_graph"""
	control = []
	case = []
	x_label = []
	y_label = []
	pvalue_label = []
	fit_data = []
	genus_data = []
	title = []
	x = []


	def __init__(self, control, case):
		super(draw_graph, self).__init__()
		self.control = control
		self.case = case

	def draw(self) :
		f, ax1 = plt.subplots(1, figsize=(14,6), dpi=80)

		plt.subplots_adjust(left=None, bottom=None, right=0.95, top=None,
		                    wspace=None, hspace=None)

		im = ax1.matshow(self.fit_data, cmap=plt.cm.Blues)
		# plt.colorbar(im, orientation='horizontal')

		plt.title(self.title)
		
		ax1.set_xticks(self.x_label)
		ax1.set_xticklabels(self.control+self.case, fontsize=7, rotation=70)
		
		#set label color
		colors = []
		for n in self.x_label :
			if self.x[n] >= len(self.control) :
				colors.append('red')
			else:
				colors.append('black')
		
		for color,tick in zip(colors,ax1.xaxis.get_major_ticks()):
			tick.label1.set_color(color) #set the color property


		ax1.xaxis.set_ticks_position('bottom')

		#y axis on left
		ax1.set_yticks(self.y_label)
		ax1.set_yticklabels(self.genus_data)
		ax2 = ax1.twinx()
		
		#y axis on right
		y_data_2 = [len(self.pvalue_label)-n-1 for n in self.y_label]
		ax2.set_yticks(y_data_2)
		ax2.set_yticklabels(self.pvalue_label)

		#set legend
		black_line = mlines.Line2D([], [], color='black',label='control')
		red_line = mlines.Line2D([], [], color='red',label='case')
		plt.legend(handles=[black_line, red_line],bbox_to_anchor=(1, 1.13), loc='upper right', borderaxespad=0.)

