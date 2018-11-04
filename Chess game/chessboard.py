#!/usr/bin/python3

try:
    import tkinter
except ImportError:
    import Tkinter as tkinter


coordinates = [[1, 2, 3, 4, 5, 6, 7, 8], ["a", "b", "c", "d", "e", "f", "g", "h"]]

# Main window
mainWindowPadding = 0
mainWindow = tkinter.Tk()
mainWindow.title("Chessboard")
mainWindow.geometry("1164x1164")
mainWindow['padx'] = mainWindow['pady'] = mainWindowPadding

# Frame to hold background image
background = tkinter.Frame(mainWindow)
background.grid(row=0, column=0, sticky="nsew", padx=0, pady=0)

# Load Background
imgPath = 'Background/OOAD630.png'
chessboardImage = tkinter.PhotoImage(file=imgPath)
imgLabel = tkinter.Label(image=chessboardImage)
# imgLabel.image = chessboardImage
imgLabel.grid(row=0, column=0, sticky="nsew", padx=0, pady=0)

# row = 0
# for sqRow in coordinates[0]:
#     if sqRow % 2 != 0:
#         for cell in range(0, 8):
#             if cell % 2 == 0:
#                 tkinter.Button(chessPad, text="Black").grid(column=cell, row=row, sticky="nsew")
#             else:
#                 tkinter.Button(chessPad, text="White").grid(column=cell, row=row, sticky="nsew")
#     else:
#         for cell in range(0, 8):
#             if cell % 2 == 1:
#                 tkinter.Button(chessPad, text="Black").grid(column=cell, row=row, sticky="nsew")
#             else:
#                 tkinter.Button(chessPad, text="White").grid(column=cell, row=row, sticky="nsew")
#
#     row += 1

mainWindow.mainloop()
