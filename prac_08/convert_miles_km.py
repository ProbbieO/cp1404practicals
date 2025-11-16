"""
CP1404
Miles to Kilometres
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934


class MilesToKilometresApp(App):
    """Convert miles to kilometres using Kivy."""
    output_km = StringProperty("0.0")

    def build(self):
        """Build the Kivy app."""
        self.title = "Miles to Kilometres Converter"
        return Builder.load_file("convert_miles_km.kv")

    def handle_convert(self):
        """Convert miles to kilometres."""
        miles = self.get_valid_miles()
        km = miles * MILES_TO_KM
        self.output_km = f"{km:.3f}"

    def handle_increment(self, change):
        """Increase or decrease miles."""
        miles = self.get_valid_miles() + change
        self.root.ids.input_miles.text = str(miles)
        self.handle_convert()

    def get_valid_miles(self):
        """Return float value, or 0 if invalid."""
        try:
            return float(self.root.ids.input_miles.text)
        except ValueError:
            return 0.0



MilesToKilometresApp().run()
