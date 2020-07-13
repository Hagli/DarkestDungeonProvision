import tkinter as tk

root = tk.Tk()

canvas = tk.Canvas(root, height = 900, width = 1000, bg = "gray1")
canvas.pack()

dungeonbutton = tk.Button(root, text = "Choose dungeon", width = 50)
dungeonbutton.pack()
dungeonbutton.place(x = 350, y = 250)

lengthbutton = tk.Button(root, text = "Choose length", width = 50)
lengthbutton.pack()
lengthbutton.place(x = 350, y = 300)

root.mainloop()