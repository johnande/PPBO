import tkinter as tk
from tkinter import Frame, Label, Entry, Button, Text, Canvas, END
from PIL import Image, ImageTk

class AplikasiMahasiswa:
    def __init__(self, root):
        self.root = root
        root.title("Data Mahasiswa Dengan Tanda Tangan")

        # Frame untuk Data Mahasiswa
        self.data_frame = Frame(root)
        self.data_frame.pack(side=tk.TOP, padx=10, pady=10)

        # Logo UGM
        image_path = "LogoUGM.png"
        img = Image.open(image_path)
        img = img.resize((img.width // 10, img.height // 10), Image.Resampling.LANCZOS)
        self.img = ImageTk.PhotoImage(img)

        # Menampilkan logo
        label_img = tk.Label(self.data_frame, image=self.img, bg='#FFFFFF')
        label_img.grid(row=0, column=0, columnspan=2, pady=5, padx=5)

        # Label dan Entry untuk Nama Mahasiswa
        self.name_label = Label(self.data_frame, text="Nama Mahasiswa:")
        self.name_label.grid(row=1, column=0, sticky=tk.W)
        self.name_entry = Entry(self.data_frame)
        self.name_entry.grid(row=1, column=1)

        # Label dan Entry untuk Nomor Mahasiswa
        self.id_label = Label(self.data_frame, text="Nomor Mahasiswa:")
        self.id_label.grid(row=2, column=0, sticky=tk.W)
        self.id_entry = Entry(self.data_frame)
        self.id_entry.grid(row=2, column=1)

        # Tombol untuk Menyimpan Data
        self.save_button = Button(self.data_frame, text="Simpan Data", command=self.save_data)
        self.save_button.grid(row=3, column=0, columnspan=2)

        # Frame untuk Tanda Tangan
        self.signature_frame = Frame(root)
        self.signature_frame.pack(side=tk.RIGHT, padx=10, pady=10)

        # Canvas untuk Tanda Tangan
        self.canvas = Canvas(self.signature_frame, width=400, height=300, bg="white")
        self.canvas.pack()

        # Tombol untuk Menghapus Canvas
        self.clear_canvas_button = Button(self.signature_frame, text="Hapus Tanda Tangan", command=self.clear_canvas)
        self.clear_canvas_button.pack()

        # Frame untuk Menampilkan Data Mahasiswa
        self.display_frame = Frame(root)
        self.display_frame.pack(side=tk.BOTTOM, padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Text widget untuk Menampilkan Data Mahasiswa
        self.text_display = Text(self.display_frame, wrap=tk.WORD, height=15)
        self.text_display.pack(expand=True, fill=tk.BOTH)

        # Bind mouse untuk menggambar di canvas
        self.canvas.bind("<B1-Motion>", self.paint)

    def clear_canvas(self):
        self.canvas.delete("all")

    def save_data(self):
        name = self.name_entry.get()
        student_id = self.id_entry.get()
        if name and student_id:
            self.text_display.insert(END, f"Nama: {name}\nNomor: {student_id}\n\n")
            self.name_entry.delete(0, END)
            self.id_entry.delete(0, END)

    def paint(self, event):
        x1, y1 = (event.x - 1), (event.y - 1)
        x2, y2 = (event.x + 1), (event.y + 1)
        self.canvas.create_oval(x1, y1, x2, y2, fill="black", outline="black")

if __name__ == "__main__":
    root = tk.Tk()
    app = AplikasiMahasiswa(root)
    root.mainloop()
