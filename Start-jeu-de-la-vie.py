import tkinter as tk
from jeu_de_la_vie.Jeu_de_la_vie import *

class App(tk.Tk):
    def __init__(self, rows, cols, refresh_delay, jeu):
        tk.Tk.__init__(self)
        self.title("Random")
        self.cellwidth = 25
        self.cellheight = self.cellwidth
        self.canvas = tk.Canvas(self, width=self.cellwidth*rows, height=self.cellheight*cols)
        self.canvas.pack(side="top", fill="both", expand="false")
        self.rows = rows
        self.cols = cols
        self.jeu = jeu

        self.rects = {}
        for column in range(self.rows):
            for row in range(self.cols):
                x1 = column*self.cellwidth
                y1 = row * self.cellheight
                x2 = x1 + self.cellwidth
                y2 = y1 + self.cellheight
                self.rects[row, column] = self.canvas.create_rectangle(x1, y1, x2, y2, tags="rect")

        self.redraw(refresh_delay)

    def redraw(self, delay):
        self.canvas.itemconfig("rect", fill="gray")
        for coordinates, alive in self.jeu.board.items():
            if alive :
                item_id = self.rects[coordinates]
                self.canvas.itemconfig(item_id, fill="black")
        self.jeu.nouveau_tour()
        self.after(delay, lambda: self.redraw(delay))

nombre_de_colonne = 50
nombre_de_ligne = 50
nombres_de_cellules_de_depart = 2000
jeu = jeu_de_la_vie(nombre_de_colonne , nombre_de_ligne, nombres_de_cellules_de_depart)
app = App(nombre_de_colonne, nombre_de_ligne, 10, jeu)
app.mainloop()
