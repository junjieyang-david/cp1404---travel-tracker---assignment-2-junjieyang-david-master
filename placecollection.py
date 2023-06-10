"""
Name:Junjie Yang
Date:08/06/2023
Brief Project Description:This file establishes the function of the PlaceCollection class of the subsequent program.
GitHub URL:https://github.com/junjieyang-david/cp1404---travel-tracker---assignment-2-junjieyang-david-master
"""


# Create your PlaceCollection class in this file
import csv
from place import *
from operator import attrgetter


class PlaceCollection:

    def __init__(self):
        self.places = None

    def load_places(self, path="places.csv"):
        """Load place objects from a csv file"""
        places = []
        with open(path, "r") as f:
            data = csv.reader(f)
            for i in data:
                p = Place(i[0], i[1], int(i[2]), i[3] == 'v')
                places.append(p)
        self.places = places
        return

    def __str__(self):
        info = ''
        if self.places == None:
            info = "The collection of places is empty"
        else:
            for p in self.places:
                info += str(p)
                info += '\n'
        return info

    def save(self, path='places.csv'):
        """Save place objects to a csv file"""
        data = []
        for p in self.places:
            data.append([p.name, p.country, p.priority, 'v' if p.is_visited else 'n'])
        with open(path, 'w', newline="") as f:
            writer = csv.writer(f)
            writer.writerows(data)
        return

    def add_place(self, p):
        """Add a single place object to the places attribute"""
        if p in self.places:
            print("%s is already in the list" % p.name)
        else:
            self.places.append(p)
        return

    def unvisited_places(self):
        """Get the number of unvisited places"""
        num = 0
        for p in self.places:
            if not p.is_visited:
                num += 1
        return num

    def sort(self, key):
        """Sort the places by the key passed in, then by priority"""
        places = self.places
        sorted_places = sorted(places, key=attrgetter(key, 'priority'))
        self.places = sorted_places
        return

