import tkinter as tk
from tkinter import messagebox
from datetime import datetime

def hitung_hari():
    try:
        tanggal_input = entry_tanggal.get()
        tanggal = datetime.strptime(tanggal_input, "%Y-%m-%d")
        sekarang = datetime.now()
        selisih = sekarang - tanggal
        jumlah_hari = selisih.days
        text_hasil.delete("1.0", tk.END)
        text_hasil.insert(tk.END, f"Jumlah hari: {jumlah_hari} hari")
        
        # Gambar canvas
        canvas.delete("all")
        canvas.create_text(100, 100, text=f"Jumlah hari: {jumlah_hari} hari", font=("Helvetica", 12))
    except ValueError:
        messagebox.showerror("Error", "Format tanggal salah! Gunakan format YYYY-MM-DD")

root = tk.Tk()
root.title("Aplikasi Hitung Hari")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

# Membuat label
label_tanggal = tk.Label(frame, text="Masukkan tanggal (YYYY-MM-DD):")
label_tanggal.grid(row=0, column=0, sticky="w")

# Membuat entry
entry_tanggal = tk.Entry(frame)
entry_tanggal.grid(row=0, column=1, padx=5)

# Membuat button
button_hitung = tk.Button(frame, text="Hitung", command=hitung_hari)
button_hitung.grid(row=0, column=2, padx=5)

# Membuat text area
text_hasil = tk.Text(frame, width=30, height=2)
text_hasil.grid(row=1, columnspan=3, pady=10)

# Membuat canvas
canvas = tk.Canvas(frame, width=200, height=200)
canvas.grid(row=2, columnspan=3, pady=10)

root.mainloop()