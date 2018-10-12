try:
    import tkinter
except ImportError:
    import Tkinter as tkinter

coordinates = [[1, 2, 3, 4, 5, 6, 7, 8], ["a", "b", "c", "d", "e", "f", "g", "h"]]

mainWindowPadding = 10

mainWindow = tkinter.Tk()
mainWindow.title("Chessboard")
mainWindow.geometry("640x640+3585-90")
mainWindow['padx'] = mainWindow['pady'] = mainWindowPadding

chessPad = tkinter.Frame(mainWindow)
chessPad.grid(row=0, column=0, sticky="nsew")

row = 0
for sqRow in coordinates[0]:
    if sqRow % 2 != 0:
        for cell in range(0, 8):
            if cell % 2 == 0:
                tkinter.Button(chessPad, text="Black").grid(column=cell, row=row, sticky="nsew")
            else:
                tkinter.Button(chessPad, text="White").grid(column=cell, row=row, sticky="nsew")
    else:
        for cell in range(0, 8):
            if cell % 2 == 1:
                tkinter.Button(chessPad, text="Black").grid(column=cell, row=row, sticky="nsew")
            else:
                tkinter.Button(chessPad, text="White").grid(column=cell, row=row, sticky="nsew")

    row += 1

mainWindow.mainloop()
