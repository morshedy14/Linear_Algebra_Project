import kivy
from kivy.app import App 
from kivy.uix.label import Label 
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button  
from kivy.uix.screenmanager import ScreenManager, Screen 
from UI.main_page import MainPage
from UI.processing_page import ProcessingPage 
from UI.load_page import LoadPage 
from UI.save_page import SavePage
from kivy.core.window import Window

import cv2 
Window.clearcolor = (44/255, 105/255, 91/255, 1)
class MyApp(App):
    def __init__(self,**kwargs):
        super(MyApp,self).__init__(**kwargs)
        self.title = "Gaussian Blurring"
        self.img = None 

    def build(self):
        self.screen_manager = ScreenManager()
        #main page 
        self.main_page = MainPage(self)
        screen = Screen(name="main")
        screen.add_widget(self.main_page)
        self.screen_manager.add_widget(screen)
        #processing page 
        self.processing_page = None
        #load page 
        self.load_page = LoadPage(self)
        screen = Screen(name="load")
        screen.add_widget(self.load_page)
        self.screen_manager.add_widget(screen)
        #save page 
        self.save_page = SavePage(self)
        screen = Screen(name="save")
        screen.add_widget(self.save_page)
        self.screen_manager.add_widget(screen)

        return self.screen_manager
    
    '''
    the function creates the processing page if already not created 
    if it is created it just updates the main scene of the processing page by the new image loaded/captured by the user
    '''
    def create_processing_page(self):
        if(self.processing_page == None):
            self.processing_page = ProcessingPage(self)
            screen = Screen(name="processing page")
            screen.add_widget(self.processing_page)
            self.screen_manager.add_widget(screen)
        else:
            self.processing_page.update_main_scene()
    
    #swtiches the screen manager of our app to the processing page 
    def switch_to_processing(self, dt):
        self.screen_manager.current = "processing page"
    
    def switch_to_load(self, dt):
        self.screen_manager.current = "load"
    
    def switch_to_save(self, dt):
        self.screen_manager.current = "save"
    
    def switch_to_main(self, dt):
        self.screen_manager.current = "main"

if __name__ == "__main__":
    app = MyApp()
    app.run()

