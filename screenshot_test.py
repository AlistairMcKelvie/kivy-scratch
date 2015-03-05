import kivy
kivy.require('1.9.0')
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.app import App
from kivy.lang import Builder
from kivy.graphics import Canvas, Translate, Fbo, ClearColor, ClearBuffers

kv = '''
cameraWidget:
    orientation: 'vertical'
    Camera:
        id: camera
        resolution: (640, 480)
        play: False
    ToggleButton:
        text: 'Play'
        on_press: camera.play = not camera.play
        size_hint_y: None
        height: '48dp'
    Button:
        text: "Take picture"
        on_press: root.TakePicture()
        height: '48dp'
'''
            
class cameraWidget(BoxLayout):
    def TakePicture(self, *args):
        print self.ids
        #self.export_to_png(self.ids.camera, filename='test2.png')
        self.ids.camera.export_to_png(filename='test2.png')

class MyApp(App):
    def build(self):
        return Builder.load_string(kv)

if __name__ == '__main__':
    MyApp().run()

