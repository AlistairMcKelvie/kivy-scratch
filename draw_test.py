import kivy
kivy.require('1.9.0')
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.graphics import Line
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from intersect import intersects, intersection_pt
from kivy.graphics.vertex_instructions import Line
from kivy.graphics import Color


kv = '''
colorAnalyzeWidget:
    orientation: 'vertical'
    Image:
        size_hint_y: None
        height: root.height * 0.75
        canvas:
            Color:
                rgba: 0, 0, 1, 1
        source: 'test2.png'
        allow_stretch: True
        keep_ratio: True
        Painter:
            size_hint_y: None
            height: root.height * 0.75
            id: painter


    BoxLayout:
        size_hint_y: None
        height: root.height * 0.25
        Button:
            text: 'Select Area'
            on_release: painter.return_points()
        Button:
            text: 'Clear'
            on_release: painter.wipe_line()
'''

class colorAnalyzeWidget(BoxLayout):
    def __init__(self, **kwargs):
        super(colorAnalyzeWidget, self).__init__(**kwargs)


class Painter(BoxLayout):
    def __init__(self, **kwargs):
        super(Painter, self).__init__(**kwargs)
        
        
    def on_touch_down(self, touch):
        self.canvas.clear()
        self.points_list = []
        with self.canvas:
            touch.ud['line'] = Line(points=(touch.x, touch.y), width=3)


    def on_touch_move(self, touch):
        touch.ud['line'].points += [touch.x, touch.y]
        self.points_list.append((touch.x, touch.y))


    def return_points(self):
        intersection_found = False
        for a in xrange(len(self.points_list)-2):
            for c in xrange(a + 2, len(self.points_list)-1):
                b = a + 1
                d = c + 1
                seg1 = (self.points_list[a], self.points_list[b])
                seg2 = (self.points_list[c], self.points_list[d])
                
                if intersects(seg1, seg2):
                    intersection_found = True
                    # todo: hand cases where intesection ins a line seg
                    intersection = intersection_pt(seg1, seg2)
                    if intersection['point']:
                        closed_poly_pts = self.points_list[b:c]
                        print "intersection['point']", intersection['point']
                        closed_poly_pts.append(intersection['point'])
                        closed_poly_pts.insert(0, intersection['point'])
                    else:
                        closed_poly_pts = self.points_list[b:c]
                        closed_poly_pts.append(intersection['seg'][0])
                        closed_poly_pts.append(intersection['seg'][1])
                        closed_poly_pts.insert(0, intersection['seg'][0])
                        closed_poly_pts.insert(0, intersection['seg'][1])
        
        if not intersection_found:
            print self.points_list
            closed_poly_pts = self.points_list
            closed_poly_pts.append(closed_poly_pts[0])
            
        closed_poly_pts = [item for pair in closed_poly_pts for item in pair]

        self.canvas.clear()
        with self.canvas:
           # draw a line using the default color
           Line(points=closed_poly_pts, width=3)


                        


    def wipe_line(self):
        self.canvas.clear()

    
class Main(App):
    def build(self):
        return Builder.load_string(kv)


if __name__ == '__main__':
    Main().run()