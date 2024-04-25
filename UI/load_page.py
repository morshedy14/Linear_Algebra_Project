import kivy
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.label import Label
from kivy.clock import Clock
from PIL import Image
import cv2


class LoadPage(GridLayout):
    def __init__(self, app, **kwargs):
        super(LoadPage, self).__init__(**kwargs)
        self.app = app
        self.cols = 1

        # file chooser
        self.file_chooser = FileChooserListView()
        self.add_widget(self.file_chooser)

        subgrid0 = GridLayout(cols=2, size_hint_y=None, height=90)

        # load button
        self.load_btn = Button(text="Load this image", background_color=(0, 0, 1, 1))
        self.load_btn.on_press = self.load_action
        subgrid0.add_widget(self.load_btn)
        # cancel button
        self.cancel_btn = Button(text="Cancel loading", background_color=(0, 0, 1, 1))
        self.cancel_btn.on_press = self.cancel_action
        subgrid0.add_widget(self.cancel_btn)

        self.add_widget(subgrid0)
        # status bar
        self.status_bar = Label(size_hint_y=None, height=50)
        self.add_widget(self.status_bar)

    def empty_status_bar(self, dt):
        self.status_bar.text = ""

    def cancel_action(self):
        Clock.schedule_once(self.app.switch_to_main, 0.5)

    '''
    checks that the file to be loaded is an image 
    reads the image if so and sets it to the app.img properity
    '''

    def load_action(self):
        if (len(self.file_chooser.selection) != 0):
            try:
                Image.open(self.file_chooser.selection[0])
                self.app.img = cv2.imread(self.file_chooser.selection[0])
                self.app.create_processing_page()
                self.status_bar.text = "Image loaded ! Switching to processing page.."

                Clock.schedule_once(self.empty_status_bar, 1)
                Clock.schedule_once(self.app.switch_to_processing, 2)

            except IOError:
                self.status_bar.text = "File chosen is not an image"
                Clock.schedule_once(self.empty_status_bar, 2)

        else:
            self.status_bar.text = "No file is chosen to load !"
