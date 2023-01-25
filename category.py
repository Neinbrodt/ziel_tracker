from tracker import tracker
import csv
import sys
from datetime import datetime
import pandas as pd
import visualization


class category:
    """Methods for handeling everything related to tracking a single category"""

    def __init__(self, name):
        # TODO: sicherstellen, dass name ein String ist
        self.name = name
        self.t = tracker()

    @staticmethod
    def start():
        print(f"Hallo!\n")
        go = input("Möchtest du eine neue Kategorie tracken? [y/n]")
        if go == "y":
            category.existence()

    @staticmethod
    def existence():
        cat_name = input("Was möchtest du tracken?")
        # Prüfe, ob die Kategorie schon existiert
        if cat_name in open("categories.csv").read():
            print("Diese Kategorie existiert schon!")
            category.existence()
        else:
            writer = csv.writer(open('categories.csv', 'a+', newline=''), delimiter=',')
            writer.writecolumn([cat_name])
            print(f"Alles klar! Du kannst jetzt {cat_name} tracken.")
            category.t_track()

    @staticmethod
    def t_track():
        go = input("Möchtest du für heute etwas tracken? [y/n]")
        if go == "y":
            print("Hier sind deine Kategorien. Wähle, indem Du eine Zahl eingibst.")
            columns = 0
            for column in open("categories.csv"):
                columns += 1
                print(f"[{columns}] - {column}")
            # TODO: Nummer hinzufügen / Datum hinzufügen zum CSV
            cat_number = int(input())
            # cat.add_today()

    def analyze(self):
        go = input("Möchtest du deine Gewohnheiten analysieren? [y/n]")
        if go == "y":
            # Die Darstellungsformen kann man ja einfach hardcoden
            vis = input(f"[1] Graph \n[2] anderes cooles Diagramm")
            if vis == "1":
                visualization.draw_graph()

    @staticmethod
    def end():
        print("byeee <3")

    # getters and setters for the category's name
    def get_name(self):
        return self.name

    def set_name(self, new_name):
        self.name = new_name

    # methods to handle data
    """add only the current date to the tracker"""

    def add_today(self):
        today = datetime.today().strftime('%Y-%m-%d')
        self.t.add_new(self, today)

    """change any date from checked to unchecked or vice-versa"""

    def change(self, date):
        if date in self.t:
            self.t.delete(self, date)
        else:
            self.t.add_new(self, date)

    """check if a date was tracked"""

    def check(self, date):
        return True if (date in self.t) else False

    # danger zone
    """clear all tracked data"""

    def clear_tracker(self):
        self.t = []

    """delete this entire tracker with all data"""

    def __del__(self):
        del self.t
