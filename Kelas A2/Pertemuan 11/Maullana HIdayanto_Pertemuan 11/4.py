import tkinter as tk
from tkinter import ttk

class SimpleGUIApp:
    def __init__(self, master):
        self.master = master
        master.title("Simple GUI App")

        # Create a frame
        self.frame = ttk.Frame(master, padding=20)
        self.frame.grid(row=0, column=0, sticky="nsew")

        # Create a label
        self.label = ttk.Label(self.frame, text="Enter some text:")
        self.label.grid(row=0, column=0, sticky="w")

        # Create an entry field
        self.entry = ttk.Entry(self.frame)
        self.entry.grid(row=1, column=0, sticky="ew")

        # Create a button
        self.button = ttk.Button(self.frame, text="Click Me", command=self.display_text)
        self.button.grid(row=2, column=0, sticky="ew")

        # Create a canvas
        self.canvas = tk.Canvas(self.frame, width=200, height=200)
        self.canvas.grid(row=0, column=1, rowspan=3, sticky="nsew")

        # Create a text box
        self.text_box = tk.Text(self.frame, height=5, width=20)
        self.text_box.grid(row=3, column=0, columnspan=2, sticky="nsew")

    def display_text(self):
        text = self.entry.get()
        self.text_box.insert("end", text + "\n")
        self.canvas.create_text(100, 100, text=text)

root = tk.Tk()
app = SimpleGUIApp(root)
root.mainloop()