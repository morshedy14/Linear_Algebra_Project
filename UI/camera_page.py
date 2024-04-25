import kivy
from kivy.app import App 
from kivy.uix.label import Label 
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button  
from kivy.uix.image import Image 
from kivy.graphics.texture import Texture
from kivy.clock import Clock
import cv2 
import numpy as np

class CameraPage(GridLayout):
    def __init__(self, app, **kwargs):
        super(CameraPage, self).__init__(**kwargs)
        self.app = app 
        self.cols = 2
        self.capture = None 
        self.ret = None 
        self.frame = None 
        self.scene = Image()
        self.add_widget(self.scene)
        
        self.capture_btn = Button(text="Capture", size_hint_y=None, height=50, background_color=(0, 0, 1, 1))
        self.capture_btn.on_press = self.capturing
        self.add_widget(self.capture_btn)
        # cancel button
        self.cancel_btn = Button(text="Cancel capturing", size_hint_y=None, height=50, background_color=(0, 0, 1, 1))
        self.cancel_btn.on_press = self.cancel_action
        self.add_widget(self.cancel_btn)

        self.status_bar = Label(size_hint_y=None,height=25)
        self.add_widget(self.status_bar)

        Clock.schedule_interval(self.update,1/60)
    def cancel_action(self):
        Clock.schedule_once(self.app.switch_to_main, 0.5)

    def update(self,dt):
        if self.app.screen_manager.current == "camera" :
            #creating a video capture in case that no capture exists 
            if self.capture == None:
                self.capture = cv2.VideoCapture(0)

            self.ret, self.frame = self.capture.read()
            # convert it to texture
            buf0 = cv2.flip(self.frame, 0)
            buf1 = buf0.tostring()
            texture = Texture.create(size=(self.frame.shape[1], self.frame.shape[0]), colorfmt='bgr') 
            #if working on RASPBERRY PI, use colorfmt='rgba' here instead, but stick with "bgr" in blit_buffer. 
            texture.blit_buffer(buf1, colorfmt='bgr', bufferfmt='ubyte')
            # display image from the texture
            self.scene.texture = texture

        elif self.capture != None:
            self.capture.release()
            self.capture = None 
        
       
    
    def empty_status_bar(self,dt):
        self.status_bar.text = ""

    def capturing(self):
        self.app.img = self.frame 
        self.status_bar.text = "Image captured! Switching to processing page.."
        self.app.create_processing_page()
        Clock.schedule_once(self.empty_status_bar,1)
        Clock.schedule_once(self.app.switch_to_processing,1) 

