import tkinter as tk
from tkinter import messagebox
import json

class Rekening:
    def __init__(self, nama):
        self.nama = nama
        self.saldo = 0
        self.catatan = []

class ManajerKeuanganModel:
    def __init__(self):
        self.rekenings = {}

class ManajerKeuanganController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def tambah_rekening(self, nama_rekening):
        if nama_rekening not in self.model.rekenings:
            self.model.rekenings[nama_rekening] = Rekening(nama_rekening)
            return True
        else:
            return False

    def tambah_pemasukan(self, nama_rekening, jumlah, keterangan):
        if nama_rekening in self.model.rekenings:
            try:
                jumlah = float(jumlah)
            except ValueError:
                return False
            rekening = self.model.rekenings[nama_rekening]
            rekening.saldo += jumlah
            rekening.catatan.append((jumlah, keterangan, 'Pemasukan'))
            self.simpan_data()
            return True
        else:
            return False

    def tambah_pengeluaran(self, nama_rekening, jumlah, keterangan):
        if nama_rekening in self.model.rekenings:
            try:
                jumlah = float(jumlah)
            except ValueError:
                return False
            rekening = self.model.rekenings[nama_rekening]
            if jumlah <= rekening.saldo: 
                rekening.saldo -= jumlah
                rekening.catatan.append((jumlah, keterangan, 'Pengeluaran'))
                self.simpan_data()
                return True
            else:
                return False
        else:
            return False
        
    def transfer_antar_rekening(self, nama_rekening_asal, nama_rekening_tujuan, jumlah, keterangan):
        if nama_rekening_asal in self.model.rekenings and nama_rekening_tujuan in self.model.rekenings:
            rekening_asal = self.model.rekenings[nama_rekening_asal]
            rekening_tujuan = self.model.rekenings[nama_rekening_tujuan]
            try:
                jumlah = float(jumlah)
            except ValueError:
                return False
            if jumlah <= rekening_asal.saldo:
                rekening_asal.saldo -= jumlah
                rekening_asal.catatan.append((-jumlah, f"Transfer ke {rekening_tujuan.nama} - {keterangan}", 'Pengeluaran'))
                rekening_tujuan.saldo += jumlah
                rekening_tujuan.catatan.append((jumlah, f"Transfer dari {rekening_asal.nama} - {keterangan}", 'Pemasukan'))
                self.simpan_data()
                return True
            else:
                return False
        else:
            return False

    def lihat_catatan(self, nama_rekening):
        if nama_rekening in self.model.rekenings:
            rekening = self.model.rekenings[nama_rekening]
            return rekening.catatan, rekening.saldo
        else:
            return None

    def lihat_semua_rekening(self):
        return [(nama_rekening, rekening.saldo) for nama_rekening, rekening in self.model.rekenings.items()]

    def simpan_data(self):
        data = {nama: {'saldo': rekening.saldo, 'catatan': rekening.catatan} for nama, rekening in self.model.rekenings.items()}
        with open('data_rekening.txt', 'w') as file:
            json.dump(data, file)

    def muat_data(self):
        try:
            with open('data_rekening.txt', 'r') as file:
                data = json.load(file)
                for nama, info in data.items():
                    rekening = Rekening(nama)
                    rekening.saldo = info['saldo']
                    rekening.catatan = info['catatan']
                    self.model.rekenings[nama] = rekening
        except FileNotFoundError:
            pass

class ManajerKeuanganView:
    def __init__(self, root, controller):
        self.root = root
        self.root.attributes("-fullscreen", True)
        self.controller = controller
        self.root.title("Spending Tracker")
        self.root.geometry("400x400")
        self.root.configure(bg='#2c3e50')

        self.main_frame = tk.Frame(root, padx=10, pady=10, width=400, height=400, bg='#f5f5f5', highlightbackground="#d4af37", highlightcolor="#d4af37", highlightthickness=2, bd=0)
        self.main_frame.pack(padx=20, pady=200)
        self.main_frame.grid_propagate(False)
        self.main_frame.grid_rowconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(0, weight=1)

        self.label = tk.Label(self.main_frame, text="Spending Tracker\nMenu:", font=("Montserrat", 18, 'bold'), fg='#2c3e50', bg='#f5f5f5')
        self.label.grid(row=0, column=0, columnspan=2, pady=(0, 20))

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

    def tampilkan_catatan(self, catatan, saldo):
        catatan_str = "\n".join([f"{transaksi[2]} - Jumlah: {transaksi[0]} - Keterangan: {transaksi[1]}" for transaksi in catatan])
        catatan_str += f"\n\nSaldo Rekening: {saldo}"
        messagebox.showinfo("Catatan Transaksi", catatan_str)

    def lihat_semua_rekening(self):
        rekenings = self.controller.lihat_semua_rekening()
        rekenings_str = "\n".join([f"Nama Rekening: {nama_rekening} - Saldo: {saldo}" for nama_rekening, saldo in rekenings])
        messagebox.showinfo("Daftar Rekening", rekenings_str)

    def tambah_rekening(self):
        self.buka_jendela_input("Tambah Rekening", ["Nama Rekening"], self.proses_tambah_rekening)

    def tambah_pemasukan(self):
        rekenings = list(self.controller.model.rekenings.keys())
        self.buka_jendela_input_dengan_pilihan("Tambah Pemasukan", ["Nama Rekening", "Jumlah", "Keterangan"], [rekenings, [], []], self.proses_tambah_pemasukan)

    def tambah_pengeluaran(self):
        rekenings = list(self.controller.model.rekenings.keys())
        self.buka_jendela_input_dengan_pilihan("Tambah Pengeluaran", ["Nama Rekening", "Jumlah", "Keterangan"], [rekenings, [], []], self.proses_tambah_pengeluaran)

    def tambah_transfer(self):
        rekenings = list(self.controller.model.rekenings.keys())
        self.buka_jendela_input_dengan_pilihan("Tambah Transfer", ["Rekening Asal", "Rekening Tujuan", "Jumlah", "Keterangan"], [rekenings, rekenings, [], []], self.proses_tambah_transfer)

    def lihat_catatan(self):
        rekenings = list(self.controller.model.rekenings.keys())
        self.buka_jendela_input_dengan_pilihan("Lihat Catatan", ["Nama Rekening"], [rekenings], self.proses_lihat_catatan)

    def buka_jendela_input(self, judul, labels, callback):
        window = tk.Toplevel(self.root)
        window.title(judul)
        window.geometry("300x200")
        window.configure(bg='#ffffff')

        input_frame = tk.Frame(window, padx=10, pady=10, bg='#ffffff')
        input_frame.pack(fill=tk.BOTH, expand=True)

        entries = {}
        for label in labels:
            tk.Label(input_frame, text=label, bg='#ffffff').pack(padx=5, pady=5)
            entry = tk.Entry(input_frame)
            entry.pack(padx=5, pady=5)
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

    def buka_jendela_input_dengan_pilihan(self, judul, labels, pilihan, callback):
        window = tk.Toplevel(self.root)
        window.title(judul)
        window.geometry("300x300")
        window.configure(bg='#ffffff')

        input_frame = tk.Frame(window, padx=10, pady=10, bg='#ffffff')
        input_frame.pack(fill=tk.BOTH, expand=True)

        entries = {}
        for i, label in enumerate(labels):
            tk.Label(input_frame, text=label, bg='#ffffff').grid(row=i, column=0, padx=5, pady=5, sticky=tk.W)
            if pilihan[i]:  # Jika ada pilihan, gunakan OptionMenu
                var = tk.StringVar(window)
                var.set(pilihan[i][0] if pilihan[i] else "")  # nilai default
                option_menu = tk.OptionMenu(input_frame, var, *pilihan[i])
                option_menu.grid(row=i, column=1, padx=5, pady=5)
                entries[label] = var
            else:  # Jika tidak ada pilihan, gunakan Entry
                entry = tk.Entry(input_frame)
                entry.grid(row=i, column=1, padx=5, pady=5)
                entries[label] = entry

        button_frame = tk.Frame(window, padx=10, pady=10, bg='#ffffff')
        button_frame.pack(fill=tk.BOTH, expand=True)

        def on_submit():
            values = {label: entry.get() if isinstance(entry, tk.Entry) else entry.get() for label, entry in entries.items()}
            window.destroy()
            callback(values)

        submit_btn = tk.Button(button_frame, text="Submit", command=on_submit, **self.button_styles)
        submit_btn.pack(side=tk.LEFT, padx=5)

        cancel_btn = tk.Button(button_frame, text="Cancel", command=window.destroy, **self.button_styles)
        cancel_btn.pack(side=tk.RIGHT, padx=5)

    def proses_tambah_rekening(self, values):
        nama_rekening = values["Nama Rekening"]
        if self.controller.tambah_rekening(nama_rekening):
            messagebox.showinfo("Sukses", "Rekening berhasil ditambahkan!")
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
        rekening_asal = values["Rekening Asal"]
        rekening_tujuan = values["Rekening Tujuan"]
        jumlah = values["Jumlah"]
        keterangan = values["Keterangan"]
        if self.controller.transfer_antar_rekening(rekening_asal, rekening_tujuan, jumlah, keterangan):
            messagebox.showinfo("Sukses", "Transfer berhasil dilakukan!")
        else:
            messagebox.showerror("Gagal", "Transfer gagal! Pastikan rekening dan jumlah valid.")

    def proses_lihat_catatan(self, values):
        nama_rekening = values["Nama Rekening"]
        catatan_saldo = self.controller.lihat_catatan(nama_rekening)
        if catatan_saldo:
            catatan, saldo = catatan_saldo
            self.tampilkan_catatan(catatan, saldo)
        else:
            messagebox.showerror("Gagal", "Rekening tidak ditemukan!")

    def konfirmasi_keluar(self):
        if messagebox.askokcancel("Keluar", "Apakah Anda yakin ingin keluar?"):
            self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    model = ManajerKeuanganModel()
    controller = ManajerKeuanganController(model, None)
    controller.muat_data()
    view = ManajerKeuanganView(root, controller)
    controller.view = view
    root.mainloop()
