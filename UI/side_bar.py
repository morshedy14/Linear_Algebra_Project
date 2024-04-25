import kivy
from kivy.app import App 
from kivy.uix.label import Label 
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button  
from kivy.uix.image import Image 
from kivy.graphics.texture import Texture
from kivy.clock import Clock
from kivy.uix.textinput import TextInput
import cv2

class SideBar(GridLayout):
    
    def __init__(self,master,**kwargs):
        super(SideBar,self).__init__(**kwargs)
        self.cols = 1
        self.common_height = 50
        self.master = master 
        
        #gaussian blur section
        self.gauss_label = Label(text="Guassian Blur")
        self.gauss_kernel_label = Label(text="Kernel Size: ")
        self.gauss_kernel_textinput = TextInput()
        self.gauss_btn = Button(text="Apply Guassian Blur")
        self.gauss_btn.on_press = self.apply_gauss
        gauss_elements = {"main_label":self.gauss_label, "kernel_label":self.gauss_kernel_label, "kernel_textinput":self.gauss_kernel_textinput,"apply_btn":self.gauss_btn}
        self.gauss_toolbox = EffectToolBox(gauss_elements)
        self.add_widget(self.gauss_toolbox)
        
        #save section 
        self.save_btn = Button(text="Save", size_hint_y=None, height=50)
        self.save_btn.on_press = self.save_action
        self.add_widget(self.save_btn)

        #switch to load page button 
        self.load_btn = Button(text="Load", size_hint_y=None, height=50)
        self.load_btn.on_press = self.back_to_load
        self.add_widget(self.load_btn)
        #status bar section 
        self.status_bar = Label(text="", size_hint_y=None, height=self.common_height)
        self.add_widget(self.status_bar)

    #removes the content of the status bar of the processing page 
    def empty_status_bar(self,dt):
        self.status_bar.text = ""  

    #saves the image after the user has applied the effects on it
    def save_action(self):
        self.status_bar.text = "saving frame..."
        Clock.schedule_once(self.empty_status_bar,1)
        Clock.schedule_once(self.master.app.switch_to_save)
    
    def back_to_load(self):
        self.status_bar.text = "Opening the load page.."
        Clock.schedule_once(self.master.app.switch_to_load,1) 
        Clock.schedule_once(self.empty_status_bar,1)

    
    def apply_gauss(self):
        if self.gauss_kernel_textinput.text != "":
            try:
                kernel_size = int(self.gauss_kernel_textinput.text.strip())
                if kernel_size % 2 != 0:
                    self.status_bar.text = "Gaussian blur applied"
                    self.master.app.img = cv2.GaussianBlur(self.master.app.img, (kernel_size, kernel_size), 0)
                    self.master.update_main_scene()
                    Clock.schedule_once(self.empty_status_bar,1)
                else:
                    self.status_bar.text = "Invalid kernel size"
                    Clock.schedule_once(self.empty_status_bar,1)
            except ValueError:
                self.status_bar.text = "Invalid kernel size"
                Clock.schedule_once(self.empty_status_bar, 1)
        else:
            self.status_bar.text = "Please add the kernel parameter"
            Clock.schedule_once(self.empty_status_bar, 1)

class EffectToolBox(GridLayout):
    def __init__(self, elements, **kwargs):
        super(EffectToolBox, self).__init__(**kwargs)
        self.cols = 1
        self.common_height = 50
        elements["main_label"].size_hint_y = None
        elements["main_label"].height = self.common_height/2
        self.add_widget(elements["main_label"])
        
        self.subGrid0 = GridLayout(size_hint_y=None, height=self.common_height)
        self.subGrid0.cols = 2

        self.subGrid0.add_widget(elements["kernel_label"])
        self.subGrid0.add_widget(elements["kernel_textinput"])

        self.add_widget(self.subGrid0)
        elements["apply_btn"].size_hint_y = None 
        elements["apply_btn"].height = self.common_height/2
        self.add_widget(elements["apply_btn"])

