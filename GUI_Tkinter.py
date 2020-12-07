import tkinter as tk


root = tk.Tk()
x = root.winfo_screenwidth()
y = root.winfo_screenheight()
root.geometry("%dx%d" % (x, y))
tk.mainloop()