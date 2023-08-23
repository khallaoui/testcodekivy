from kivy.app import App
from kivy.core.window import Window
from kivy.core.audio import SoundLoader
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager
from kivy.base import runTouchApp
from kivy.uix.image import Image

Window.clearcolor = (89 / 255.0, 7 / 255.0, 45, 3)
Window.size = (400, 600)


class Res(Screen):
    pass


class Error(Screen):
    pass


class Mod(Screen):
    pass


class Not(Screen):
    pass


class Etu(Screen):
    pass


class Aut(Screen):
    pass


class Est(Screen):
    pass


class Ensa(Screen):
    pass


class Fs(Screen):
    pass

class Encg(Screen):
    pass


class W1(Screen):
    pass


class W2(Screen):
    pass


class Wm(ScreenManager):
    pass


kv = Builder.load_file('test2kv.kv')


class MyAPP(App):
    def build(self):
        self.title = 'Universite Ibn Tofail'
        return kv


if __name__ == '__main__':
    MyAPP().run()
