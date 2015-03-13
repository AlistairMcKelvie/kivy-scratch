import kivy
kivy.require('1.8.0') 

from kivy.app import App
from kivy.graphics import Line
from kivy.uix.widget import Widget


class DrawInput(Widget):
    def on_touch_down(self, touch):
        print(touch)
        with self.canvas:
            touch.ud['line'] = Line(points=(touch.x, touch.y))
        
    
    def on_touch_move(self, touch):
        print(touch)
        touch.ud['line'].points += (touch.x, touch.y)
        
        
    def on_touch_up(self, touch):
        print('released', touch)



class test(App):
    def build(self):
        return DrawInput()


if __name__ == '__main__':
    test().run()