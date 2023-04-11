from kivy.config import Config
from kivymd.app import MDApp
from kivymd.uix.screenmanager import ScreenManager
from kivy.lang import Builder

class Ui(ScreenManager):
    pass

class MainApp(MDApp):
    def build(self):
        self.icon = "./assets/IMG_E2702.JPG"
        self.theme_cls.theme_style ="Light"
        self.theme_cls.primary_palette = 'DeepPurple'
        self.theme_cls.accent_palette = 'Red'
        Builder.load_file("desing.kv")
        return Ui()
    def on_start(self):
        Config.set('graphics', 'width', '360')
        Config.set('graphics', 'height', '640')
    def cambiar_tema(self, checked, value):
        if value:
            self.theme_cls.theme_style='Dark'
        else:
            self.theme_cls.theme_style="Light"

if __name__ == '__main__':
    MainApp().run()