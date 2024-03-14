import re
import urllib
from datetime import time
import json
import threading
import httplib2
import requests
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
import matplotlib.pyplot as plt
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
from matplotlib.figure import Figure


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
			text: "Solution conductance"
			pos_hint: {"center_x": 0.5, "center_y": 0.5}
			font_style: "H4"
			halign: "center"
	MDBoxLayout:
		id: graph_box                      
		size_hint: 1, 0.9
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
		        font_name: "Arial"
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
		        font_name: "Arial"
		        id: c_max          
		        text: "text"
		        pos_hint: {"center_x": 0.7, "center_y": 0.5}                                        
		MDFloatLayout:
			canvas:
				Color:                        
	                rgba: 0, 1, 1, 0.1    
		        Rectangle:                    
		            size: self.size         
		            pos: self.pos
		    pos_hint: {"center_x": 0.8, "center_y": 0.5}   
		    size_hint: 0.25, 1
		    MDLabel:
		        font_name: "Arial"
		        id: c_avr          
		        text: "text"
		        pos_hint: {"center_x": 0.7, "center_y": 0.5}                               
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
		        font_name: "Arial"
		        id: c_min          
		        text: "text"
		        pos_hint: {"center_x": 0.7, "center_y": 0.5}                                        
'''
class Main_window(MDBoxLayout):

	def __init__(self, **kwargs):
		super().__init__(**kwargs)

		self.graf = plt.gcf()
		self.graph = None
		self.x_axes = []
		self.y_axes = []
		self.t = 0
		self.y_value = 0
		self.bind(on_kv_post=self.create_graph)
		Clock.schedule_once(self.init_serial_connection)

	# creating of plot
	def create_graph(self, *args):
		graph_box = self.ids.graph_box
		graph_box.add_widget(FigureCanvasKivyAgg(self.graf))

 	# attempt of threading
	def init_serial_connection(self, *args):
		threading.Thread(target=self.start_bar_plotting, daemon=True).start()

	#----connecting to Arduino bouard via com3 port
	def start_bar_plotting(self):
		try:    # try / except  prevents of crashing program
			self.Ard_Data = serial.Serial("com3", 9600)  # com3 port for USB connection
			Clock.schedule_interval(self.on_start, 1)

		except serial.SerialException:
			Clock.schedule_once(self.retry_connection, 0.1)

	def retry_connection(self, dt):
		self.start_bar_plotting()

	# retrieving data from arduino and treating it
	def on_start(self, dt):
		self.read_data = self.Ard_Data.readline()
		self.read_data = self.read_data.decode()
		self.digits = re.findall(r'\b\d+\.\d+\b', self.read_data)
		self.read_data_t = float(self.digits[0])
		self.read_data_t = round(self.read_data_t, 3)
		self.y_axes.append(self.read_data_t)
		self.t += dt
		self.t = round(self.t)
		self.x_axes.append(self.t)
		self.y_value = max(self.y_axes)+0.025

		# setting of plots properties
		plt.legend(["ϰ/t"], loc="upper right")
		plt.plot(self.x_axes, self.y_axes,
			color='red',
			linestyle='-',
			linewidth=3,
			animated=False,
	    	markerfacecolor='blue',
			markersize=12)

		plt.xlabel('t, sec')
		plt.ylabel('ϰ, 1/R')
		plt.grid(False)
		plt.ylim(0, self.y_value)
		plt.style.context('dark_background')
		self.graf.canvas.draw()

		# adding new variables
		min_value = min(self.y_axes)
		min_value = round(min_value, 3)
		max_value = max(self.y_axes)
		max_value = round(max_value, 3)
		avr_value = sum(self.y_axes)/len(self.y_axes)
		avr_value = round(avr_value, 3)
		actual_value = self.y_axes[-1]

		self.ids.c_min.text = "ϰ min " + str(min_value) + " S/cm"
		self.ids.c_max.text = "ϰ max " + str(max_value) + " S/cm"
		self.ids.c_avr.text = "ϰ avr " + str(avr_value) + " S/cm"
		self.ids.c_act.text = "ϰ " + str(actual_value)  + " S/cm"

		# preparing data for sending to remote web server
		data = {
			'x_axes': self.x_axes,
			'y_axes': self.y_axes
				}
		url = 'http://conductivity.atwebpages.com/save_data.php'

		headers = {"Content-Type": "application/json", "charset": "UTF-8"}

		response = requests.post(url, json=data, headers=headers)

class Conductivity(MDApp):
	def build(self):
		self.theme_cls.theme_style = "Light"
		self.theme_cls.primary_palette = "Green"
		self.theme_cls.material_style = "M3"
		return Builder.load_string(KV)


if __name__ == '__main__':
	Conductivity().run()



	#Main_window.task3.start()