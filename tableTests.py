import tkinter as tk
import random


class App(tk.Tk):
    def __init__(self, rows, cols, refresh_delay):
        tk.Tk.__init__(self)
        self.title("Random")
        self.cellwidth = 25
        self.cellheight = self.cellwidth
        self.canvas = tk.Canvas(self, width=self.cellwidth*rows, height=self.cellheight*cols)
        self.canvas.pack(side="top", fill="both", expand="false")
        self.rows = rows
        self.cols = cols

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
        for i in range(10):
            row = random.randint(0, self.rows - 1)
            col = random.randint(0, self.cols - 1)
            item_id = self.rects[row, col]
            self.canvas.itemconfig(item_id, fill="black")
        self.after(delay, lambda: self.redraw(delay))


app = App(50, 50, 10)
app.mainloop()
