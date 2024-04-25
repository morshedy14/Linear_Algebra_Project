import kivy
from kivy.app import App 
from kivy.uix.label import Label 
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button  
from kivy.uix.image import Image 
from kivy.graphics.texture import Texture
from kivy.clock import Clock
from kivy.uix.textinput import TextInput 
from UI.side_bar import SideBar
import cv2 
import numpy as np 

class ProcessingPage(GridLayout):

    def __init__(self,app,**kwargs):
        super(ProcessingPage,self).__init__(**kwargs)
        self.app = app
        
        self.img_texture = ""
        self.convert_to_texture()
        
        self.cols = 2
        self.orientation = "lr-tb"
        
        self.main_scene = Image(texture = self.img_texture)
        self.add_widget(self.main_scene)

        self.side_bar = SideBar(self)
        self.side_bar.size_hint_x = None 
        self.side_bar.width = 250
        self.add_widget(self.side_bar)

    #converts the image(numpy array) to the appropriate formate to be read by the image object of kivy
    def convert_to_texture(self,colorfmt="bgr"):
        buf0 = cv2.flip(self.app.img,0)
        buf1 =  buf0.tostring() 
        self.img_texture = Texture.create(size=(self.app.img.shape[1],self.app.img.shape[0]),colorfmt=colorfmt)
        self.img_texture.blit_buffer(buf1, colorfmt=colorfmt, bufferfmt='ubyte')
        return self.img_texture

    #updates the frame displayed on the image object in the processing page 
    def update_main_scene(self):
        self.convert_to_texture()
        self.main_scene.texture = self.img_texture

    