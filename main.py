import re
from datetime import time

import serial
from kivy.clock import Clock
from kivy.lang import Builder
from kivy_garden.graph import Graph
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivy_garden.graph import BarPlot, Graph, SmoothLinePlot, LinePlot, MeshLinePlot
from kivymd.uix.label import MDLabel
KV = '''
Main_window:
	
#<Main_window>:
	id: box
	orientation: "vertical"
	MDBoxLayout:
		canvas:
			Color:                        
                rgba: 1, 0, 0, 0.1    
	        Rectangle:                    
	            size: self.size         
	            pos: self.pos
            
		size_hint: 1, 0.1
		MDLabel:
			text: "Solution conductivity"
			pos_hint: {"center_x": 0.5, "center_y": 0.5}
			font_style: "H4"
			halign: "center"
	MDBoxLayout:
		id: graph_box
		#canvas:
		#	Color:                        
        #        rgba: 0, 0, 1, 0.1    
	    #    Rectangle:                    
	    #        size: self.size         
	    #        pos: self.pos
		size_hint: 0.95, 0.9
	MDBoxLayout:      
	
		size_hint: 1, 0.1 	
		MDFloatLayout:  
			canvas:
				Color:                        
	                rgba: 0, 1, 0, 0.1    
		        Rectangle:                    
		            size: self.size         
		            pos: self.pos
		    pos_hint: {"center_x": 0.25, "center_y": 0.5}    
		    size_hint: 0.25, 1                              
		    MDLabel:
		        id: c_act                                           
		        text: "text"
		        pos_hint: {"center_x": 0.8, "center_y": 0.5}                                 
		    
		    	
		 	
		MDFloatLayout:
			canvas:
				Color:                        
	                rgba: 1, 1, 0, 0.1    
		        Rectangle:                    
		            size: self.size         
		            pos: self.pos
		    pos_hint: {"center_x": 0.5, "center_y": 0.5}           
		    size_hint: 0.25, 1
		    MDLabel:
		        id: c_max          
		        text: "text"
		        pos_hint: {"center_x": 0.8, "center_y": 0.5}                                        
		MDFloatLayout:
			canvas:
				Color:                        
	                rgba: 0, 1, 1, 0.1    
		        Rectangle:                    
		            size: self.size         
		            pos: self.pos
		    pos_hint: {"center_x": 0.75, "center_y": 0.5}   
		    size_hint: 0.25, 1
		    MDLabel:
		        id: c_avr          
		        text: "text"
		        pos_hint: {"center_x": 0.8, "center_y": 0.5}                               
		MDFloatLayout:                    
			canvas:                       
				Color:                    
		            rgba: 0.75, 1, 1, 1    
		        Rectangle:                
		            size: self.size       
		            pos: self.pos
		    pos_hint: {"center_x": 0.9, "center_y": 0.5}   
		    size_hint: 0.25, 1
		    MDLabel:
		        id: c_min          
		        text: "text"
		        pos_hint: {"center_x": 0.9, "center_y": 0.5}                                        
'''
class Main_window(MDBoxLayout):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		#print(self.children)
		self.graph = None
		self.x_axes = []
		self.y_axes = []
		self.t = 0
		
		self.bind(on_kv_post=self.create_graph)

	def create_graph(self, *args):
		# This method will be called after the KV rules are applied
		#self.graph = Graph(
			# Your graph configuration...
		#)
		# Find the box layout with id graph_box
		self.graph = Graph(
			xlabel='time',
			ylabel='λ, 1/R',
			border_color=(0, 0, 0, 1),
			label_options={'color': (0, 0, 0, 1)},
			x_ticks_minor=1,
			x_ticks_major=5,
			y_ticks_major=1,
			y_ticks_minor=1,
			#y_ticks_major=5,
			y_grid_label=True,
			x_grid_label=True,
			padding=5,
			x_grid=False,
			y_grid=False,
			xmin=0, xmax=60,
			ymin=0, ymax=3,
			pos_hint={"x": 0, "y": 0.05},
			size_hint=(0.5, 0.9)
		)

		self.plot = SmoothLinePlot(color=[0, 1, 0, 1])
		self.plot_x = self.x_axes
		self.plot_y = self.y_axes
		#self.plot.color = [0, 1, 0, 1]
		# self.graph.add_plot(self.plot2)
		self.graph.add_plot(self.plot)
		graph_box = self.ids.graph_box
		graph_box.add_widget(self.graph)
		self.start_bar_plotting()

	def start_bar_plotting(self):
		try:
			self.Ard_Data = serial.Serial("com3", 9600)  # com3 port for USB connection
			Clock.schedule_interval(self.on_start, 1)
			#Clock.schedule_interval(self.update_axis, 1)
			Clock.schedule_interval(self.update_points, 0.25)

		except serial.SerialException:
			Clock.schedule_once(self.retry_connection, 0.1)

	def retry_connection(self, dt):
		self.start_bar_plotting()

	def bar_plot_stop(self):
		Clock.unschedule(self.on_start)
		#Clock.unschedule(self.update_axis)
		#Clock.unschedule(self.update_points)
		time.sleep(0.5)
		self.Ard_Data.close()

	def on_start(self, dt):
		self.read_data = self.Ard_Data.readline()
		self.read_data = self.read_data.decode()
		#print(self.read_data)
		self.digits = re.findall(r'\b\d+\.\d+\b', self.read_data)
		#print(self.digits[0])   #-------------------> to debug output
		#try:
		self.read_data_t = float(self.digits[0])

		self.y_axes.append(self.read_data_t)
		#print(self.y_axes)
	    #
		#except:

	#	self.radiation.append(self.read_data_r)
	#	# self.coordinates.append(self.read_data_c)
	#	# self.temperature.append(self.read_data_t)
	#
	#	self.read_data_r = 60 * self.read_data_r
	#	self.y_axes.append(self.read_data_r)
	#
		self.t += dt
		self.t = round(self.t)
	#
		self.x_axes.append(self.t)
	#
		if len(self.x_axes) > 50:
		#	self.x_axes.pop(0)
			Clock.schedule_interval(self.update_axis, 1)
		#if len(self.y_axes) > 50:
		#	self.y_axes.pop(0)
	#
		print(self.x_axes)
		print(self.y_axes)
		min_value = min(self.y_axes)
		min_value = round(min_value, 3)
		max_value = max(self.y_axes)
		max_value = round(max_value, 3)
		avr_value = sum(self.y_axes)/len(self.y_axes)
		avr_value = round(avr_value, 3)
		actual_value = self.y_axes[-1]

		self.ids.c_min.text = "λ min " + str(min_value)
		self.ids.c_max.text = "λ max " + str(max_value)
		self.ids.c_avr.text = "λ avr " + str(avr_value)
		self.ids.c_act.text = "λ " + str(actual_value)

	def update_axis(self, dt):
		self.graph.xmin = self.x_axes[0]
		self.graph.xmax = self.x_axes[-1]
	
	def update_points(self, *args):
		self.plot.points = [(self.x_axes[i], self.y_axes[i]) for i in range(len(self.y_axes))]

class Conductivity(MDApp):
	def build(self):
		self.theme_cls.theme_style = "Light"
		self.theme_cls.primary_palette = "Green"
		self.theme_cls.material_style = "M3"
		return Builder.load_string(KV)



Conductivity().run()