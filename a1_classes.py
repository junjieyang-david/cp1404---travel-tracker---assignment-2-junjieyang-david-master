"""
Name:Junjie Yang
Date:07/06/2023
Brief Project Description:
GitHub URL:https://github.com/JCUS-CP1404/cp1404---travel-tracker---assignment-2-junjieyang-david
"""
# Copy your first assignment to this file, then update it to use Place class
# Optionally, you may also use PlaceCollection class

import csv

import place
from place import Place
from placecollection import PlaceCollection
import random


MENU = "Menu:\nL - List places\nR - Recommend random place\nA - Add new place\nM - Mark a place as visited\nQ - Quit"
FILE_NAME = "places.csv"


def main():
    print("Welcome to Travel Tracker 2.0-designed by Junjie Yang")
    place_collection = PlaceCollection()
    place_collection.load_places(FILE_NAME)
    print(f"{len(place_collection.places)} places loaded from places.csv")
    print(MENU)
    menu_choice = input(">>>").upper()
    while menu_choice != "Q":
        if menu_choice == "L":
            # list_places(places)
            place_collection.sort("is_visited")
            print(place_collection)
        elif menu_choice == "R":
            recommend_place(places)
        elif menu_choice == "A":
            add_place(places)
        elif menu_choice == "M":
            mark_visited(places)
        else:
            print("Invalid menu choice")
        print(MENU)
        menu_choice = input(">>>").upper()
    place_collection.save()
    print(f"{len(place_collection.places)} places saved to {FILE_NAME}")
    print("Have a nice day :)")


# def list_places(places):
#     counting = 0
#     visited = 0
#     data_sorter = sorted(places, key=lambda row: (row[3], int(row[2])))
#     for a in data_sorter:
#         if a[3] == "n":
#             print("*{0:>2}.{1:<10} in {2:<12} priority {3:>5}".format(counting + 1, a[0], a[1], a[2]))
#             visited += 1
#         else:
#             print(" {0:>2}.{1:<10} in {2:<12} priority {3:>5}".format(counting + 1, a[0], a[1], a[2]))
#         counting += 1
#     if visited == 0:
#         print("{0} places. No places left to visit. Why not add a new place?".format(counting))
#     else:
#         print("{0} places. You still want to visit {1} places.".format(counting, visited))


def recommend_place(places):
    unvisited_places = [place for place in places if place[3] == "n"]
    if not unvisited_places:
        print("No places left to visit!")
        return
    place = random.choice(unvisited_places)
    print("Not sure where to visit next?")
    print(f"How about... {place[0]} in {place[1]}?")


def add_place(places):
    name = input("Name: ")
    while name.strip() == " ":
        print("Input can not be blank")
        name = input("Name: ")
    country = input("Country: ")
    while country.strip() == " ":
        print("Input can not be blank")
        country = input("Country: ")
    priority = input("Priority: ")
    while not priority.isdigit() or int(priority) < 1:
        priority = input("Priority: ")
    print(f"{name} in {country}(priority {priority}) added to Travel Tracker")
    places.append([name, country, int(priority), "n"])


def mark_visited(places):
    unvisited_places = [place for place in places if place[3] == "n"]
    if not unvisited_places:
        print("No unvisited places")
        return
    list_places(places)
    counter = 0
    data_sorter = sorted(places, key=lambda row: (row[3], int(row[2])))
    print("Enter the number of a place to mark as visited")

    while True:
        try:
            user_input = int(input(">>> "))
            if user_input <= 0:
                print("Number must be > 0")
                continue
            elif user_input > len(places):
                print("Invalid place number")
                continue
            elif not check_place_mark(user_input, places):
                print("That Place is already visited")
            break
        except ValueError:
            print("Invalid Input; Enter a valid number")

    for row in data_sorter:
        counter = counter + 1
        if counter == int(user_input):
            if row[3] != "v":
                print("{} in {} visited!".format(row[0], row[1]))
            row[3] = "v"


def check_place_mark(user_input, places):
    data_sorter = sorted(places, key=lambda row: (row[3], int(row[2])))
    count_place = 0
    for row in data_sorter:
        count_place += 1
        if count_place == int(user_input):
            if row[3] == "v":
                return False
            else:
                return True


main()

