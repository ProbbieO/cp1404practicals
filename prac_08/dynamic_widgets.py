"""
CP1404 - Practical 08
Dynamic Labels

"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.properties import StringProperty

NEW_COLOUR = (1, 0, 0, 1)  # RGBA for red
ALTERNATIVE_COLOUR = (1, 0, 1, 1)  # RGBA for magenta


class DynamicWidgetsApp(App):
    """Main program - Kivy app to demo dynamic widget creation."""
    status_text = StringProperty()

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        # list of names
        self.names = ["Paul", "Robbie", "Omuyoma", "JCU", "1404"]


    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_widgets.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        """Create labels and add them to the GUI."""
        for name in self.names:
            label = Label(text=name)
            self.root.ids.entries_box.add_widget(label)

    def press_entry(self, instance):
        """Handle pressing entry buttons."""
        # get name (dictionary key) from the text of Button we clicked on
        name = instance.text
        # change the button's background colour
        instance.background_color = ALTERNATIVE_COLOUR
        # update status text
        self.status_text = f"You selected: {name}"


    def clear_all(self):
        """Clear all widgets that are children of the "entries_box" layout widget."""
        self.root.ids.entries_box.clear_widgets()


DynamicWidgetsApp().run()