"""
Name:Junjie Yang
Date:07/06/2023
Brief Project Description:This file establishes the function of the Place class of the subsequent program.
GitHub URL:https://github.com/junjieyang-david/cp1404---travel-tracker---assignment-2-junjieyang-david-master
"""


# Create your Place class in this file


class Place:
    """Represent a place object."""

    def __init__(self, name="", country="", priority=0, is_visited=False):
        """Initialise a Place instance.
        name: str
        country: str
        priority: int
        visited_status: bool
        """
        self.name = name
        self.country = country
        self.priority = priority
        self.is_visited = is_visited
        return

    def __str__(self):
        """Show the information about the place"""
        if self.is_visited:
            info = """%s in %s, priority %s (visited) """ %(self.name, self.country, self.priority)
        else:
            info = """%s in %s, priority %s """ %(self.name, self.country, self.priority)
        return info

    def visit(self):
        """Mark the place as visited"""
        self.is_visited = True
        return

    def unvisited(self):
        """Mark the place as unvisited"""
        self.is_visited = False
        return

    def is_important(self):
        """To determine if the place is considered "important" """
        return int(self.priority <= 2)

