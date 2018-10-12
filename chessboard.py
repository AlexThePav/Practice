try:
    import tkinter
except ImportError:
    import Tkinter as tkinter

colors = ["Black", "White"]
coordinates = [["1", "2", "3", "4", "5", "6", "7", "8"], ["a", "b", "c", "d", "e", "f", "g", "h"]]

mainWindowPadding = 10

mainWindow = tkinter.Tk()
mainWindow.title("Chessboard")
mainWindow.geometry("640x640+3585-90")
mainWindow['padx'] = mainWindow['pady'] = mainWindowPadding

chessPad = tkinter.Frame(mainWindow)
chessPad.grid(row=0, column=0, sticky="nsew")

row = 0
for sqRow in coordinates[0]:
    for black in range(0, 9, 2):
        tkinter.Button(chessPad, text=colors[0]).grid(column=black, row=row, sticky="nsew")
    for white in range(1, 9, 2):
        tkinter.Button(chessPad, text=colors[1]).grid(column=white, row=row, sticky="nsew")
    row += 1

mainWindow.mainloop()
