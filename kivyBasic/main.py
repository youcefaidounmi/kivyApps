from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class boxLayoutEx(BoxLayout):
    pass

class mainWidget(Widget):
    pass

class kivyBasicApp(App):
    def build(self):
        return boxLayoutEx()

if __name__ == '__main__':
    app = kivyBasicApp()
    app.run()