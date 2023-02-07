import tkinter as tk
##from tkinter import ttk
##import pickle
import random
import time
import os
##import sqlite3
import webbrowser

launch = True
##file = open('Index.txt')

while(launch == True):
    try:
        print(launch)
        window = tk.Tk()
        window.title("Music Index")
##        window.resizable(0, 0) <- makes it unresizable
        canvas = tk.Canvas(window, width=400, height=800, bd=0, highlightthickness=0)
        canvas.pack()
        window.update()
        launch = False
        break
    except:
        print("Canvas/Window Failed to be made")
        x = 400
print(launch)

##conn = sqlite3.connect('Index.db')
##
##print('index loaded')  #sqlite3
##
##print(conn)

class Song:
    def __init__(self):
##        self.id = tk.Listbox()
        self.id = canvas.create_ectangle(0, 50, 400, 800, fill='grey')
    def select(self, start, end):
        None

class Top:
    def __init__(self):
        self.id = tk.Menu()
##        self.id = canvas.create_rectangle(0, 0, 400, 50, fill='gray')

class Scroll:
    def __init__(self, canvas):
        self.id = tk.Scrollbar() #tkk

song = Song()
top = Top()
scroll = Scroll(canvas)
window.update()
window.attributes('-alpha', 0.995)
window.iconbitmap('C://Users//super//Downloads//pythontutorial-1-150x150.ico')

##while True:
##    window.config(width=(random.randint(0, 1000)), height=(random.randint(0, 1000)))
##    time.sleep(1)
##    window.update()
