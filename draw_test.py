import kivy
kivy.require('1.9.0')
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.graphics import Line
from kivy.uix.widget import Widget


kv = '''
colorAnalyzeWidget:
    Painter
'''

class colorAnalyzeWidget(BoxLayout):
    class Painter(Widget):
        def on_touch_down(self, touch):
            with self.canvas:
                touch.ud['line'] = Line(points=(touch.x, touch.y))


        def on_touch_move(self, touch):
            touch.ud['line'].points += [touch.x, touch.y]

            
class Main(App):
    def build(self):
        return Builder.load_string(kv)


if __name__ == '__main__':
    presentation = Builder.load_string(kv)
    Main().run()