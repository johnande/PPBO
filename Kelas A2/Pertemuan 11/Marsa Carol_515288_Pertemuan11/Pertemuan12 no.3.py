import tkinter as tk
from tkinter import messagebox

class TicketApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi Pembelian Tiket Wisata")
        
        # Frame untuk informasi tiket
        self.frame_info = tk.Frame(root)
        self.frame_info.pack(pady=10)

        self.label_title = tk.Label(self.frame_info, text="Pembelian Tiket Wisata", font=("Arial", 16))
        self.label_title.pack()

        self.label_name = tk.Label(self.frame_info, text="Nama:")
        self.label_name.pack(anchor='w')

        self.entry_name = tk.Entry(self.frame_info)
        self.entry_name.pack(fill='x')

        self.label_ticket_type = tk.Label(self.frame_info, text="Jenis Tiket:")
        self.label_ticket_type.pack(anchor='w')

        self.label_adult_quantity = tk.Label(self.frame_info, text="Jumlah Tiket Dewasa (Rp 75.000):")
        self.label_adult_quantity.pack(anchor='w')

        self.entry_adult_quantity = tk.Entry(self.frame_info)
        self.entry_adult_quantity.pack(fill='x')

        self.label_child_quantity = tk.Label(self.frame_info, text="Jumlah Tiket Anak-anak (Rp 40.000):")
        self.label_child_quantity.pack(anchor='w')

        self.entry_child_quantity = tk.Entry(self.frame_info)
        self.entry_child_quantity.pack(fill='x')

        # Frame untuk tombol aksi
        self.frame_action = tk.Frame(root)
        self.frame_action.pack(pady=10)

        self.button_submit = tk.Button(self.frame_action, text="Beli Tiket", command=self.submit)
        self.button_submit.pack(side='left', padx=5)

        self.button_clear = tk.Button(self.frame_action, text="Clear", command=self.clear)
        self.button_clear.pack(side='left', padx=5)

        # Canvas untuk gambar (contoh saja, tidak ada gambar sebenarnya)
        self.canvas = tk.Canvas(root, width=200, height=100, bg='lightgray')
        self.canvas.pack(pady=10)

        # Frame untuk hasil
        self.frame_result = tk.Frame(root)
        self.frame_result.pack(pady=10)

        self.text_result = tk.Text(self.frame_result, height=10, width=50)
        self.text_result.pack()

    def submit(self):
        name = self.entry_name.get()
        adult_quantity = self.entry_adult_quantity.get()
        child_quantity = self.entry_child_quantity.get()
        
        if not name or not adult_quantity.isdigit() or not child_quantity.isdigit():
            messagebox.showerror("Error", "Mohon isi semua data dengan benar!")
            return
        
        adult_quantity = int(adult_quantity)
        child_quantity = int(child_quantity)
        
        adult_price = 75000
        child_price = 40000
        total_price = (adult_quantity * adult_price) + (child_quantity * child_price)
        
        result = (f"Nama: {name}\n"
                  f"Jumlah Tiket Dewasa: {adult_quantity}\n"
                  f"Jumlah Tiket Anak-anak: {child_quantity}\n"
                  f"Total Harga: Rp {total_price}")
        
        self.text_result.delete(1.0, tk.END)
        self.text_result.insert(tk.END, result)
        messagebox.showinfo("Success", "Pembelian tiket berhasil!")

    def clear(self):
        self.entry_name.delete(0, tk.END)
        self.entry_adult_quantity.delete(0, tk.END)
        self.entry_child_quantity.delete(0, tk.END)
        self.text_result.delete(1.0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = TicketApp(root)
    root.mainloop()
