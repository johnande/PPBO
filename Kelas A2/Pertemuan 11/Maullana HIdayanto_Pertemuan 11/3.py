import tkinter as tk

class SimpleNotesApp:
    def __init__(self, master):
        self.master = master
        master.title("Simple Notes App")

        # Frame for input section
        self.input_frame = tk.Frame(master)
        self.input_frame.pack(pady=10)

        self.label = tk.Label(self.input_frame, text="Enter your note:")
        self.label.pack(side=tk.LEFT, padx=5)

        self.entry = tk.Entry(self.input_frame, width=50)
        self.entry.pack(side=tk.LEFT, padx=5)

        self.add_button = tk.Button(self.input_frame, text="Add Note", command=self.add_note)
        self.add_button.pack(side=tk.LEFT, padx=5)

        # Canvas for displaying notes
        self.canvas = tk.Canvas(master, width=400, height=300, bg="white")
        self.canvas.pack(pady=10)

        # Text widget for detailed note view
        self.text_widget = tk.Text(master, width=50, height=10)
        self.text_widget.pack(pady=10)

        # Initialize note list
        self.notes = []
    
    def add_note(self):
        note = self.entry.get()
        if note:
            self.notes.append(note)
            self.update_canvas()
            self.entry.delete(0, tk.END)
    
    def update_canvas(self):
        self.canvas.delete("all")
        for i, note in enumerate(self.notes):
            self.canvas.create_text(10, 20 + i*20, anchor=tk.W, text=note, tags=f"note_{i}")
            self.canvas.tag_bind(f"note_{i}", "<Button-1>", lambda e, i=i: self.show_note_detail(i))
    
    def show_note_detail(self, index):
        self.text_widget.delete(1.0, tk.END)
        self.text_widget.insert(tk.END, self.notes[index])

root = tk.Tk()
app = SimpleNotesApp(root)
root.mainloop()
