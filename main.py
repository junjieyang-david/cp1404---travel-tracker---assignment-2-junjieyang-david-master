"""
Name:Junjie Yang
Date:07/06/2023
Brief Project Description: Travel Tracker Program Assignment 2
GitHub URL:https://github.com/JCUS-CP1404/cp1404---travel-tracker---assignment-2-junjieyang-david
"""

# Create your main program in this file, using the TravelTrackerApp class

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button

from placecollection import PlaceCollection
from place import Place

path='places.csv'
visited_color = (1, 1, 1, 0.6)
unvisited_color = (0, 1, 0.8, 0.7)

class PlacesApp(App):
    """..."""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.pc = PlaceCollection() # get a single PlaceCollection object

    def build(self):
        """Build Travel Tracker App """
        self.title = "Travel Tracker"
        self.root = Builder.load_file('app.kv')
        try:
            self.pc.load(path)
            self.top_bar()
            self.bottom_bar("Welcome to Travel Tracker")
            self.places_list()
        # Failed to find the file
        except (FileNotFoundError, LookupError):
            self.top_bar()
            self.bottom_bar("Could not find places.csv!")
        return self.root

    def top_bar(self):
        """Show the number of places still to visit"""
        num = self.pc.unvisited_places()
        self.root.ids.top_bar.text = "Places to visit: %s" % num
        return

    def bottom_bar(self,content):
        """Show program messages"""
        self.root.ids.bottom_bar.text = content
        return

    def places_list(self,key='is_visited'):
        """Get sorted places list and create button for each of them"""
        self.pc.sort(key)
        self.root.ids.place_list.clear_widgets()  # clear widgets
        for p in self.pc.places:
            # set the text and color for each place
            btn = Button(text=str(p),background_color= visited_color if p.is_visited else unvisited_color)
            btn.bind(on_release=self.click)
            btn.place = p # Store a reference to the place object in the button object
            self.root.ids.place_list.add_widget(btn)

    def click(self,btn):
        """Change between visit & unvisited when user click the button"""
        p = btn.place
        # change button's text and color
        if p.is_visited:
            p.unvisited()
            btn.text = str(p)
            btn.background_color = unvisited_color
        else:
            p.visit()
            btn.text = str(p)
            btn.background_color = visited_color

        # change the bottom bar content
        if p.is_important() == 1:
            if p.is_visited:
                self.bottom_bar("You visited %s. Great travelling!" % p.name)
            else:
                self.bottom_bar("You need to visit %s. Get going!" % p.name)
        else:
            if p.is_visited:
                self.bottom_bar("You visited %s." % p.name)
            else:
                self.bottom_bar("You need to visit %s." % p.name)

        # change the top bar content
        self.top_bar()
        return

    def add(self, name_input, country_input, priority_input):
        """Handle Add New Book..."""
        # error checking
        name, country, priority = map(str.strip, (name_input.text, country_input.text, priority_input.text))
        if not name and not country and not priority:
            self.bottom_bar("All fields must be completed")
            return
        else:
            # check if priority field a valid integer
            try:
                priority = int(priority)
            except ValueError:
                self.bottom_bar("Please enter a valid number")
                return
            # check if the input page is greater than 0
            if priority < 1:
                self.bottom_bar("Priority must be > 0")
                return

        p = Place(name, country, priority)
        self.pc.add(p)
        self.places_list()
        self.top_bar()
        self.bottom_bar("%s has been added to Travel Tracker." % name)
        self.clear_input_field(name_input, country_input, priority_input)
        return

    @staticmethod
    def clear_input_field(name_input, country_input, priority_input):
        """Clear the user inputs fields"""
        name_input.text = ''
        country_input.text = ''
        priority_input.text = ''

    def on_stop(self):
        """Save an updated places list file when the app is closed"""
        self.pc.save(path)
        return super().on_stop()

if __name__ == '__main__':
    PlacesApp().run()
