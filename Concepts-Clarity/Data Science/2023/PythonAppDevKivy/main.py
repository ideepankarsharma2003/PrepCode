import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
import random

kivy.require('1.9.0')
# BUILDOZER

class MyRoot(BoxLayout):
    def __init__(self):
        print("calling super constructor")
        super(MyRoot, self).__init__()
    
    def generate_number(self):
        self.random_label.text= str(random.randint(0, 1000))



class RandomNumberGenerator(App):
    def build(self):
        # return Label(text='Hello world')
        # return BoxLayout()
        # print("calling MyRoot")
        return MyRoot()



neuralRandom= RandomNumberGenerator()
neuralRandom.run()