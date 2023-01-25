import csv

import tracker
import numpy as np
import pandas as pd

import plotly.express as px

t = []

global row_name
global currentFrame
currentFrame = pd.DataFrame()
row_name = '0'


def add_list(self):
    global dr
    dr = pd.DataFrame(t)
    dr = dr.rename(columns={0: row_name})


def new_list():
    row_name = input("Wie soll die Spalte heißen?")
    for x in range(var):
        answer = input("Wähle eine Zahl.")
        t.append(answer)
        print(t)
        if x != var - 1:
            add_list(t)
            print(dr)
        else:
            answer = input("Möchtest du eine weitere Spalte eingeben? (Y/N)")
            if answer == "Y" or answer == "y":
                new_list()
            else:
                drawing()
                frames.append(t)


def printer():
    global currentFrame
    print("Was möchtest du printen?")
    print(frames)
    answer = input()
    if answer in frames:
        currentFrame = pd.DataFrame.transform(answer)
        print(currentFrame)
    else:
        print("Das gibbet nicht!")
        printer()


def drawing():
    global currentFrame
    # goals = pd.DataFrame({'x_data': t, 'y_data': [1, 2, 3]})
    fig = px.line(currentFrame, x=row_name, title="Testing")
    fig.show()


def draw_graph():
    df = pd.read_csv("categories.csv")
    print(f"Was möchtest du analysieren?")
    print("Hier sind deine Kategorien. Wähle, indem Du eine Zahl eingibst.")
    with open("categories.csv", "r") as cat_list:
        reader = csv.reader(cat_list)
        i = next(reader)
        print(i)
    cat_number = int(input())
    fig = px.line(df[cat_number + 1:], title="Testing")
    fig.show()


def list():
    print("Lege eine neue Liste an!")
    global var
    var = input("Wie viele Rows soll die Liste haben?")
    var = int(var)
    new_list()


class Work:
    draw_graph()
