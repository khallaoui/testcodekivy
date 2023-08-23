from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp



class MainApp(MDApp):
    def build(self):
        screen = Screen()
        table = MDDataTable(
            column_data=[
                ("first name", dp(30)),
                ("Secon name", dp(30)),
                ("E-Mail", dp(30)),
                ("Phone", dp(30))
            ],
        )
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Blue"
        screen.add_widget(table)
        return screen

if __name__=="__main__" :
    MainApp().run()
