import tkinter as tk
from tkinter import colorchooser

class SimplePaintApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Paint App")

        self.color = 'black'
        self.brush_size = 5

        # Frame for options
        self.options_frame = tk.Frame(self.root, padx=10, pady=10)
        self.options_frame.pack(side=tk.LEFT, fill=tk.Y)

        # Brush size label and entry
        self.size_label = tk.Label(self.options_frame, text="Brush Size:")
        self.size_label.pack(pady=5)
        self.size_entry = tk.Entry(self.options_frame, width=5)
        self.size_entry.insert(0, '5')
        self.size_entry.pack(pady=5)

        # Color button
        self.color_button = tk.Button(self.options_frame, text="Choose Color", command=self.choose_color)
        self.color_button.pack(pady=5)

        # Clear button
        self.clear_button = tk.Button(self.options_frame, text="Clear Canvas", command=self.clear_canvas)
        self.clear_button.pack(pady=5)

        # Canvas for drawing
        self.canvas = tk.Canvas(self.root, bg='white', width=600, height=400)
        self.canvas.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        self.canvas.bind('<B1-Motion>', self.paint)

        # Instructions label
        self.instructions = tk.Label(self.options_frame, text="Click and drag to draw", wraplength=150)
        self.instructions.pack(pady=20)

        # Text widget for additional notes
        self.notes_label = tk.Label(self.options_frame, text="Notes:")
        self.notes_label.pack(pady=5)
        self.notes_text = tk.Text(self.options_frame, width=20, height=10)
        self.notes_text.pack(pady=5)

    def choose_color(self):
        self.color = colorchooser.askcolor(color=self.color)[1]

    def clear_canvas(self):
        self.canvas.delete("all")

    def paint(self, event):
        self.brush_size = int(self.size_entry.get())
        x1, y1 = (event.x - self.brush_size), (event.y - self.brush_size)
        x2, y2 = (event.x + self.brush_size), (event.y + self.brush_size)
        self.canvas.create_oval(x1, y1, x2, y2, fill=self.color, outline=self.color)

if __name__ == "__main__":
    root = tk.Tk()
    app = SimplePaintApp(root)
    root.mainloop()
