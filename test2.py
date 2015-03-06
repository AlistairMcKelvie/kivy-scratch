import kivy
kivy.require('1.8.0') 

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.widget import Widget
from kivy.graphics import Line

kv_file = 'test.kv'


class Painter(Widget):
    def on_touch_down(self, touch):
        with self.canvas:
            touch.ud['line'] = Line(points=(touch.x, touch.y))


    def on_touch_move(self, touch):
        touch.ud['line'].points += [touch.x, touch.y]


class MainScreen(Screen):
    pass
    

class AnotherScreen(Screen):
    pass
    
    
class ScreenManagement(ScreenManager):
    pass
    

class Main(App):
    def build(self):
        return presentation 


if __name__ == '__main__':
    presentation = Builder.load_string(kv_file)
    Main().run()