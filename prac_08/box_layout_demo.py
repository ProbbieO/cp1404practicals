"""
CP1404 - Practical08
Clear and Greet buttons
"""

from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    """Main App for greeting demo."""

    def build(self):
        """Build the Kivy app."""
        self.title = "Greeter App"
        return Builder.load_file('box_layout.kv')

    def handle_greet(self):
        """Handle greeting button press."""
        print("Greet button pressed")
        name = self.root.ids.input_name.text
        if name.strip():
            self.root.ids.output_label.text = f"Hello {name}"
        else:
            self.root.ids.output_label.text = "Hello!"

    def handle_clear(self):
        """Handle clear button press."""
        print("Clear button pressed")
        # Reset the label
        self.root.ids.output_label.text = "Enter your name"





BoxLayoutDemo().run()
