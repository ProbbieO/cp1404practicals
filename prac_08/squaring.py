"""
CP1404 Practical 08
square number
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

__author__ = 'Lindsay Ward'


class SquareNumberApp(App):
    """ SquareNumberApp is a Kivy App for squaring a number """
    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (200, 100)
        self.title = "Square Number"
        self.root = Builder.load_file('squaring.kv')
        return self.root

    def handle_calculate(self):
        """ handle calculation (could be button press or other call), output result to label widget """
        try:
            value = self.get_valid_number(self.root.ids.input_number.text)
            result = float(value) ** 2
            self.root.ids.output_label.text = str(result)
        except ValueError:
            pass

    def get_valid_number(self,text):
        """Return an int from text, or 0 if invalid."""
        try:
            return int(text)
        except ValueError:
            return 0


SquareNumberApp().run()