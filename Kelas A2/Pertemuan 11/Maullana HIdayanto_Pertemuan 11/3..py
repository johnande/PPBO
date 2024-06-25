import tkinter as tk
from tkinter import Canvas, Label, Button, Entry, Text, Frame

class SimpleApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Drawing App")

        # Frame untuk input
        self.input_frame = Frame(root)
        self.input_frame.pack(pady=10)

        # Label dan Entry untuk lebar
        self.width_label = Label(self.input_frame, text="Width:")
        self.width_label.grid(row=0, column=0, padx=5)
        self.width_entry = Entry(self.input_frame)
        self.width_entry.grid(row=0, column=1, padx=5)

        # Label dan Entry untuk tinggi
        self.height_label = Label(self.input_frame, text="Height:")
        self.height_label.grid(row=1, column=0, padx=5)
        self.height_entry = Entry(self.input_frame)
        self.height_entry.grid(row=1, column=1, padx=5)

        # Tombol untuk menggambar persegi panjang
        self.draw_button = Button(self.input_frame, text="Draw Rectangle", command=self.draw_rectangle)
        self.draw_button.grid(row=2, column=0, columnspan=2, pady=10)

        # Canvas untuk menggambar
        self.canvas = Canvas(root, width=400, height=400, bg="white")
        self.canvas.pack(pady=20)

        # Frame untuk pesan
        self.message_frame = Frame(root)
        self.message_frame.pack(pady=10)

        # Label dan Text untuk pesan
        self.message_label = Label(self.message_frame, text="Messages:")
        self.message_label.pack(side="left", padx=5)
        self.message_text = Text(self.message_frame, height=5, width=50)
        self.message_text.pack(side="left", padx=5)

    def draw_rectangle(self):
        try:
            # Mendapatkan lebar dan tinggi dari Entry
            width = int(self.width_entry.get())
            height = int(self.height_entry.get())

            # Menghapus gambar sebelumnya
            self.canvas.delete("all")

            # Menggambar persegi panjang di tengah kanvas
            x0 = (400 - width) / 2
            y0 = (400 - height) / 2
            x1 = x0 + width
            y1 = y0 + height
            self.canvas.create_rectangle(x0, y0, x1, y1, fill="blue")

            # Menampilkan pesan sukses
            self.message_text.insert(tk.END, f"Successfully drew a rectangle of width {width} and height {height}.\n")
        except ValueError:
            # Menampilkan pesan error jika input tidak valid
            self.message_text.insert(tk.END, "Error: Please enter valid integers for width and height.\n")

# Membuat dan menjalankan aplikasi
root = tk.Tk()
app = SimpleApp(root)
root.mainloop()
