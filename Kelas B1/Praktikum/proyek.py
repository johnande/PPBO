import tkinter as tk
from tkinter import messagebox

class CustomApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Custom Tkinter App")
        self.root.geometry("400x300")

        # Menambahkan Label
        self.label = tk.Label(root, text="Selamat Datang di Custom Tkinter App", font=("Arial", 14), fg="blue")
        self.label.pack(pady=10)

        # Menambahkan Entry
        self.entry_label = tk.Label(root, text="Masukkan Nama Anda:", font=("Arial", 12))
        self.entry_label.pack(pady=5)
        self.name_entry = tk.Entry(root, font=("Arial", 12))
        self.name_entry.pack(pady=5)

        # Menambahkan Button
        self.submit_button = tk.Button(root, text="Submit", command=self.submit_name, font=("Arial", 12), bg="green", fg="white")
        self.submit_button.pack(pady=10)

        # Menambahkan Listbox
        self.listbox_label = tk.Label(root, text="Daftar Nama:", font=("Arial", 12))
        self.listbox_label.pack(pady=5)
        self.name_listbox = tk.Listbox(root, font=("Arial", 12), height=5)
        self.name_listbox.pack(pady=5)

        # Menambahkan Exit Button
        self.exit_button = tk.Button(root, text="Exit", command=root.quit, font=("Arial", 12), bg="red", fg="white")
        self.exit_button.pack(pady=10)

    def submit_name(self):
        name = self.name_entry.get()
        if name:
            self.name_listbox.insert(tk.END, name)
            self.name_entry.delete(0, tk.END)
            messagebox.showinfo("Success", f"Nama '{name}' berhasil ditambahkan!")
        else:
            messagebox.showwarning("Warning", "Nama tidak boleh kosong.")

if __name__ == "__main__":
    root = tk.Tk()
    app = CustomApp(root)
    root.mainloop()
