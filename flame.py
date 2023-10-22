import tkinter as tk
from tkinter import *

# These lines of code are creating a window for the Flame Game application.
window = Tk()
window.title("Flame Game")
window.geometry("500x500")

Label(window, text="Play Flame Game", font=("san-serif", 20)).pack()
Label(window, text="Enter Your Name").pack()

n1 = tk.StringVar()
n2 = tk.StringVar()


def Flames():
    """
    The function "Flames" takes two names as input, calculates a number based on the names, and assigns
    a relationship status based on that number.
    """
    name1 = n1.get()
    name2 = n2.get()

    nameString = name1 + name2
    for c in nameString:
        if nameString.count(c) != 1:
            nameString = nameString.replace(c, "")

    number = len(nameString) % 6

    global rel
    rel = ""

    if number == 1:
        rel += "Friends"
    elif number == 2:
        rel += "Love"
    elif number == 3:
        rel += "Affection"
    elif number == 4:
        rel += "Marriage"
    elif number == 5:
        rel += "Enemy"
    elif number == 0:
        rel += "Siblings"
    else:
        pass

    Label(window, text="According to the Game of Flames the relation is:").pack()
    Label(window, text=rel).pack()


Entry(window, textvariable=n1).pack()
Label(window, text="Enter Your Cruse's Name").pack()
Entry(window, textvariable=n2).pack()

Button(window, text="Show Result", bg="light blue", command=Flames).pack()

window.mainloop()
