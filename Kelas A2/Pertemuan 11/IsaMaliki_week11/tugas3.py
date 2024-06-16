import tkinter as tk
from tkinter import messagebox

class BMICalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Kalkulator BMI")
        self.root.geometry("400x400")

        # Frame untuk form
        self.frame_form = tk.Frame(self.root, padx=10, pady=10)
        self.frame_form.pack(pady=20)

        # Label dan Entry untuk berat badan
        self.label_berat = tk.Label(self.frame_form, text="Berat Badan (kg):")
        self.label_berat.grid(row=0, column=0, pady=5)
        self.entry_berat = tk.Entry(self.frame_form)
        self.entry_berat.grid(row=0, column=1, pady=5)

        # Label dan Entry untuk tinggi badan
        self.label_tinggi = tk.Label(self.frame_form, text="Tinggi Badan (cm):")
        self.label_tinggi.grid(row=1, column=0, pady=5)
        self.entry_tinggi = tk.Entry(self.frame_form)
        self.entry_tinggi.grid(row=1, column=1, pady=5)

        # Tombol untuk menghitung BMI
        self.button_hitung = tk.Button(self.frame_form, text="Hitung BMI", command=self.hitung_bmi)
        self.button_hitung.grid(row=2, columnspan=2, pady=10)

        # Canvas untuk menampilkan hasil BMI
        self.canvas = tk.Canvas(self.root, width=300, height=100, bg="lightyellow")
        self.canvas.pack(pady=20)

        # Text widget untuk menampilkan log operasi
        self.text_output = tk.Text(self.root, height=5, width=40)
        self.text_output.pack(pady=20)

    def hitung_bmi(self):
        try:
            berat = float(self.entry_berat.get())
            tinggi = float(self.entry_tinggi.get()) / 100  # konversi ke meter
            bmi = berat / (tinggi ** 2)
            kategori = self.kategori_bmi(bmi)

            # Menampilkan hasil di Canvas
            self.canvas.delete("all")  # Menghapus konten sebelumnya
            self.canvas.create_text(150, 50, text=f"BMI: {kategori}", font=("Times New Roman", 16), fill="red")

            # Menampilkan log operasi di Text widget
            self.text_output.insert(tk.END, f"Berat: {berat} kg, Tinggi: {tinggi*100:.1f} cm\nBMI: {bmi:.2f} ({kategori})\n")
        except ValueError:
            messagebox.showwarning("Peringatan", "Harap masukkan angka yang valid untuk berat dan tinggi badan.")

    def kategori_bmi(self, bmi):
        if bmi < 18.5:
            return "Kurus"
        elif 18.5 <= bmi < 24.9:
            return "Normal"
        elif 25 <= bmi < 29.9:
            return "Kelebihan Berat Badan"
        else:
            return "Obesitas"

if __name__ == "__main__":
    root = tk.Tk()
    app = BMICalculatorApp(root)
    root.mainloop()
