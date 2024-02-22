from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout

KV = '''
Main_window:
<Main_window>:
	orientation: "vertical"
	MDBoxLayout:
		canvas:
			Color:                        
                rgba: 1, 0, 0, 0.1    
	        Rectangle:                    
	            size: self.size         
	            pos: self.pos
            
		size_hint: 1, 0.1
	MDBoxLayout:
		canvas:
			Color:                        
                rgba: 0, 0, 1, 0.1    
	        Rectangle:                    
	            size: self.size         
	            pos: self.pos
		size_hint: 1, 0.8
	MDBoxLayout:
		canvas:
			Color:                        
                rgba: 0, 1, 0, 0.1    
	        Rectangle:                    
	            size: self.size         
	            pos: self.pos
		size_hint: 1, 0.1



'''

class Main_window(MDBoxLayout):
	pass

class Conductivity(MDApp):
	def build(self):
		return Builder.load_string(KV)



Conductivity().run()