import tkinter as tk
from tkinter import messagebox

class ManajerKeuanganView:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.root.title("Spending Tracker")

        # Main Frame
        self.main_frame = tk.Frame(root, padx=10, pady=10, width=300, height=360, bg='#f5f5f5', 
                                   highlightbackground="#d4af37", highlightcolor="#d4af37", highlightthickness=2, bd=0)
        self.main_frame.pack(padx=20, pady=20)
        self.main_frame.grid_propagate(False)
        self.main_frame.grid_rowconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(0, weight=1)

        # Label
        self.label = tk.Label(self.main_frame, text="Spending Tracker\nMenu:", font=("Montserrat", 18, 'bold'), 
                              fg='#2c3e50', bg='#f5f5f5')
        self.label.grid(row=0, column=0, columnspan=2, pady=(0, 20))

        # Button Styles
        self.button_styles = {
            "background": "#2c3e50",
            "foreground": "#ffffff",
            "highlightbackground": "#ffffff",
            "highlightcolor": "#ffffff",
            "highlightthickness": 2,
            "bd": 0,
            "relief": "flat",
            "font": ("Montserrat", 11)
        }

        # Buttons
        self.tambah_rekening_btn = tk.Button(self.main_frame, text="Tambah Rekening", width=25, command=self.tambah_rekening, **self.button_styles)
        self.tambah_rekening_btn.grid(row=1, column=0, pady=5)
        self.tambah_pemasukan_btn = tk.Button(self.main_frame, text="Tambah Pemasukan", width=25, command=self.tambah_pemasukan, **self.button_styles)
        self.tambah_pemasukan_btn.grid(row=2, column=0, pady=5)
        self.tambah_pengeluaran_btn = tk.Button(self.main_frame, text="Tambah Pengeluaran", width=25, command=self.tambah_pengeluaran, **self.button_styles)
        self.tambah_pengeluaran_btn.grid(row=3, column=0, pady=5)
        self.tambah_transfer_btn = tk.Button(self.main_frame, text="Tambah Transfer", width=25, command=self.tambah_transfer, **self.button_styles)
        self.tambah_transfer_btn.grid(row=4, column=0, pady=5)
        self.lihat_catatan_btn = tk.Button(self.main_frame, text="Lihat Catatan Transaksi", width=25, command=self.lihat_catatan, **self.button_styles)
        self.lihat_catatan_btn.grid(row=5, column=0, pady=5)
        self.lihat_semua_rekening_btn = tk.Button(self.main_frame, text="Lihat Semua Rekening", width=25, command=self.lihat_semua_rekening, **self.button_styles)
        self.lihat_semua_rekening_btn.grid(row=6, column=0, pady=5) 
        self.keluar_btn = tk.Button(self.main_frame, text="Keluar", width=25, command=self.konfirmasi_keluar, **self.button_styles)
        self.keluar_btn.grid(row=7, column=0, pady=(5, 0))

    # Display transaction records
    def tampilkan_catatan(self, catatan):
        catatan_str = "\n".join([f"{transaksi[2]} - Jumlah: {transaksi[0]} - Keterangan: {transaksi[1]}" for transaksi in catatan])
        messagebox.showinfo("Catatan Transaksi", catatan_str)

    # View all accounts
    def lihat_semua_rekening(self):
        rekenings = self.controller.lihat_semua_rekening()
        rekenings_str = "\n".join([f"Nama Rekening: {nama_rekening} - Saldo: {saldo}" for nama_rekening, saldo in rekenings])
        messagebox.showinfo("Daftar Rekening", rekenings_str)

    # Add new account
    def tambah_rekening(self):
        self.buka_jendela_input("Tambah Rekening", ["Nama Rekening"], self.proses_tambah_rekening)

    # Add new income
    def tambah_pemasukan(self):
        self.buka_jendela_input("Tambah Pemasukan", ["Nama Rekening", "Jumlah", "Keterangan"], self.proses_tambah_pemasukan)

    # Add new expense
    def tambah_pengeluaran(self):
        self.buka_jendela_input("Tambah Pengeluaran", ["Nama Rekening", "Jumlah", "Keterangan"], self.proses_tambah_pengeluaran)

    # Add new transfer
    def tambah_transfer(self):
        self.buka_jendela_input("Tambah Transfer", ["Rekening Asal", "Rekening Tujuan", "Jumlah", "Keterangan"], self.proses_tambah_transfer)

    # View account transactions
    def lihat_catatan(self):
        self.buka_jendela_input("Lihat Catatan", ["Nama Rekening"], self.proses_lihat_catatan)

    # Open input window
    def buka_jendela_input(self, judul, labels, callback):
        window = tk.Toplevel(self.root)
        window.title(judul)
        window.geometry("300x200")
        window.configure(bg='#ffffff')

        input_frame = tk.Frame(window, padx=10, pady=10, bg='#ffffff')
        input_frame.pack(fill=tk.BOTH, expand=True)
        
        entries = {}
        
        for i, label in enumerate(labels):
            tk.Label(input_frame, text=label, bg='#ffffff').grid(row=i, column=0, padx=5, pady=5, sticky=tk.W)
            entry = tk.Entry(input_frame)
            entry.grid(row=i, column=1, padx=5, pady=5)
            entries[label] = entry

        button_frame = tk.Frame(window, padx=10, pady=10, bg='#ffffff')
        button_frame.pack(fill=tk.BOTH, expand=True)
        
        def on_submit():
            values = {label: entry.get() for label, entry in entries.items()}
            window.destroy()
            callback(values)

        submit_btn = tk.Button(button_frame, text="Submit", command=on_submit, **self.button_styles)
        submit_btn.pack(side=tk.LEFT, padx=5)

        cancel_btn = tk.Button(button_frame, text="Cancel", command=window.destroy, **self.button_styles)
        cancel_btn.pack(side=tk.RIGHT, padx=5)

    def proses_tambah_rekening(self, values):
        nama_rekening = values["Nama Rekening"]
        if self.controller.tambah_rekening(nama_rekening):
            messagebox.showinfo("Sukses", f"Rekening '{nama_rekening}' berhasil dibuat!")
        else:
            messagebox.showerror("Gagal", "Rekening sudah ada!")

    def proses_tambah_pemasukan(self, values):
        nama_rekening = values["Nama Rekening"]
        jumlah = values["Jumlah"]
        keterangan = values["Keterangan"]
        if self.controller.tambah_pemasukan(nama_rekening, jumlah, keterangan):
            messagebox.showinfo("Sukses", "Pemasukan berhasil ditambahkan!")
        else:
            messagebox.showerror("Gagal", "Rekening tidak ditemukan atau jumlah tidak valid!")

    def proses_tambah_pengeluaran(self, values):
        nama_rekening = values["Nama Rekening"]
        jumlah = values["Jumlah"]
        keterangan = values["Keterangan"]
        if self.controller.tambah_pengeluaran(nama_rekening, jumlah, keterangan):
            messagebox.showinfo("Sukses", "Pengeluaran berhasil ditambahkan!")
        else:
            messagebox.showerror("Gagal", "Rekening tidak ditemukan atau jumlah tidak valid!")

    def proses_tambah_transfer(self, values):
        nama_rekening_asal = values["Rekening Asal"]
        nama_rekening_tujuan = values["Rekening Tujuan"]
        jumlah = values["Jumlah"]
        keterangan = values["Keterangan"]
        if self.controller.transfer_antar_rekening(nama_rekening_asal, nama_rekening_tujuan, jumlah, keterangan):
            messagebox.showinfo("Sukses", "Transfer berhasil dilakukan!")
        else:
            messagebox.showerror("Gagal", "Transfer gagal dilakukan. Pastikan nama rekening dan jumlah yang dimasukkan benar!")

    def proses_lihat_catatan(self, values):
        nama_rekening = values["Nama Rekening"]
        catatan_saldo = self.controller.lihat_catatan(nama_rekening)
        if catatan_saldo:
            catatan, saldo = catatan_saldo
            self.tampilkan_catatan(catatan)
        else:
            messagebox.showerror("Gagal", "Rekening tidak ditemukan!")

    def konfirmasi_keluar(self):
        konfirmasi = messagebox.askokcancel("Konfirmasi Keluar", "Apakah Anda yakin ingin keluar?")
        if konfirmasi:
            self.keluar()

    def keluar(self):
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("400x400")
    root.configure(bg='#2c3e50')
    model = ManajerKeuanganModel()
    controller = ManajerKeuanganController(model, None)
    view = ManajerKeuanganView(root, controller)
    controller.view = view
    controller.muat_data() 
    root.mainloop()
