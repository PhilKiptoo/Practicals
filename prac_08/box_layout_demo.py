"""
CP1404/CP5632 Practical - BoxLayout Demo.
"""

from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    """BoxLayoutDemo is a Kivy App to demonstrate basic box layouts."""

    def build(self):
        """Build the Kivy app from the kv file."""
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        """Greet the user by name from input_name text input."""
        self.root.ids.output_label.text = f"Hello {self.root.ids.input_name.text}"

    def handle_clear(self):
        """Clear both the input_name text input and the output_label label."""
        self.root.ids.input_name.text = ""
        self.root.ids.output_label.text = ""


BoxLayoutDemo().run()
