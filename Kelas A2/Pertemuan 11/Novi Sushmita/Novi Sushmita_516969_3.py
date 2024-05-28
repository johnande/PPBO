import tkinter as tk

def kirim_resep():
    nama_pasien = entry_nama_pasien.get()
    resep = text_resep.get("1.0", tk.END)
    label_resep.config(text=f"RESEP\n ============ \n{nama_pasien}\n ============ \n{resep} ============")

root = tk.Tk()
root.title("Aplikasi Resep Dokter")

frame = tk.Frame(root)
frame.pack()

canvas_logo = tk.Canvas(frame, width=50, height=50, bg="light blue", highlightthickness=0)
canvas_logo.grid(row=0, column=0, padx=5, pady=5)
canvas_logo.create_oval(5, 5, 45, 45, fill="blue")

label_nama_perusahaan = tk.Label(frame, text="RSI Yogyakarya", font=("Helvetica", 14))
label_nama_perusahaan.grid(row=0, column=1, padx=5, pady=5)

label_nama_pasien = tk.Label(frame, text="Nama Pasien:")
label_nama_pasien.grid(row=1, column=0, padx=5, pady=5, sticky="e")

entry_nama_pasien = tk.Entry(frame)
entry_nama_pasien.grid(row=1, column=1, padx=5, pady=5)

text_resep = tk.Text(root, height=10, width=30)
text_resep.pack()

button_print = tk.Button(root, text="Print", command=kirim_resep)
button_print.pack()

label_resep = tk.Label(root, text="", anchor="w")
label_resep.pack()

root.mainloop()