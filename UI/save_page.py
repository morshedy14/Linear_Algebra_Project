import kivy
from kivy.uix.gridlayout import GridLayout 
from kivy.uix.button import Button 
from kivy.uix.filechooser import FileChooserIconView 
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.clock import Clock
import cv2 
import os 

class SavePage(GridLayout):
    def __init__(self, app, **kwargs):
        super(SavePage, self).__init__(**kwargs)
        self.app = app 
        self.cols = 1
        self.padding = 10
        #file chooser
        self.file_chooser = FileChooserIconView()
        self.add_widget(self.file_chooser)
        #save textinput (takes in the name to save by)
        self.save_text_input = TextInput()
        #save button 
        self.save_btn = Button(text="save this image", background_color=(0, 0, 1, 1))
        self.save_btn.on_press = self.save_action
        #status bar
        self.status_bar = Label(size_hint_y=None,height=30)

        save_section = GridLayout(cols=2,size_hint_y=None,height=40)
        save_section.add_widget(self.save_text_input)
        save_section.add_widget(self.save_btn)
        self.add_widget(save_section)
        self.add_widget(self.status_bar)

    def empty_status_bar(self,dt):
        self.status_bar.text = ""
    
    def save_action(self):
        if self.save_text_input.text != "":
           filename = self.save_text_input.text.strip() + ".jpg"
           cv2.imwrite(os.path.join(self.file_chooser.path, filename),self.app.img)
           self.status_bar.text = "Image saved at "+ os.path.join(self.file_chooser.path,self.save_text_input.text)
           Clock.schedule_once(self.app.switch_to_processing, 2)
           Clock.schedule_once(self.empty_status_bar, 3)
        else:
            self.status_bar.text = "type some name to save the image by"
            Clock.schedule_once(self.empty_status_bar, 2)
