import tkinter as tk

root = tk.Tk()
root.title("GUI window")
# create a geometry for the window
root.geometry("300x200")
#adding a label to the window
label = tk.Label(root, text="Hello, welcome to the GUI window!")
label.pack()
#execute tkinter
root.mainloop()