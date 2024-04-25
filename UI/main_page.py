import kivy
from kivy.app import App 
from kivy.uix.label import Label 
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button  
from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager, Screen 
from UI.processing_page import ProcessingPage 
import cv2 
import numpy as np 

class MainPage(GridLayout):
    def __init__(self, app, **kwargs):
        super(MainPage, self).__init__(**kwargs)
        
        self.app = app 
        
        self.cols = 1
        self.padding = 50
        self.spacing = 10
        self.add_widget(Label(text="Welcome to Image Blurring Prompt"))

        self.load_img_btn = Button(text="Load  Image", background_color=(0, 0, 1, 1))
        self.load_img_btn.on_press = self.load_img 
        self.add_widget(self.load_img_btn)

        self.status_bar = Label()
        self.status_bar.height = 30
        self.add_widget(self.status_bar)
    
#removes the content of the status bar of the main page.
    def empty_status_bar(self, *_):
        self.status_bar.text = ""
          
    #function for loading image that is going to be processed 
    def load_img(self):
        self.status_bar.text = "Opening load page.."      
        Clock.schedule_once(self.empty_status_bar, 1)
        Clock.schedule_once(self.app.switch_to_load, 1)
