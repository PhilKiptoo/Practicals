"""
CP1404/CP5632 Practical - Dynamic Labels.
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    """DynamicLabelsApp is a Kivy App to dynamically display labels for names."""

    def __init__(self, **kwargs):
        """Initialise the app with a list of names."""
        super().__init__(**kwargs)
        self.names = ["Alice", "Bob", "Charlie", "David", "Eve"]

    def build(self):
        """Build the Kivy app and dynamically create labels."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create a Label widget for each name in the names list."""
        for name in self.names:
            temp_label = Label(text=name)
            self.root.ids.main.add_widget(temp_label)


DynamicLabelsApp().run()
