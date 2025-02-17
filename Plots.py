import tkinter as tk
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import matplotlib.colors as pltc
from random import sample

class HomeWindowGraph(tk.Frame):
    #Class to create the plot at the Home Window
    def __init__ (self, parent, mainWinObj):
        tk.Frame.__init__(self)
        self.mainWinObj = mainWinObj
        all_colors = [k for k,v in pltc.cnames.items()]
        #all_colors = list(self.mainWinObj.allAcc.categoriesColor.values())
        Categories = list(self.mainWinObj.allAcc.categoriesColor.keys())
        Values = (12, 40, 70, 35, 26, 40, 70, 35, 26)
        #colors = sample(all_colors, 5)
        f = Figure()#figsize=(5,1))
        a = f.add_subplot(111)
        a.bar(Categories, Values, color=all_colors)
        a.set_facecolor('xkcd:mint green')
        f.patch.set_facecolor('xkcd:mint green')
        self.canvas = FigureCanvasTkAgg(f, parent)
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(row = 0, column =1, sticky="nswe")

