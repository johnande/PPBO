from tkinter import Tk, Label, Button, Entry, Frame, Text, Canvas, W, E, END

class BMI_Kalkulator:
    def __init__(self, master):
        master.title("BMI Kalkulator")
        self.frame = Frame(master)
        self.frame.pack()
        self.label_tinggi = Label(self.frame, text="Tinggi Badan (cm):")
        self.entry_tinggi = Entry(self.frame)
        self.label_berat = Label(self.frame, text="Berat Badan (kg): ")
        self.entry_berat = Entry(self.frame)
        self.jumlah = Button(self.frame, text="Menghitung BMI", command=self.menghitung_bmi)
        self.tampilan = Text(self.frame, height=5, width=30)
        self.canvas = Canvas(master, width=400, height=50)

        # Layout
        self.label_tinggi.grid(row=0, column=0, sticky=W)
        self.entry_tinggi.grid(row=0, column=1, columnspan=2, sticky=W+E)
        self.label_berat.grid(row=1, column=0, sticky=W)
        self.entry_berat.grid(row=1, column=1, columnspan=2, sticky=W+E)
        self.jumlah.grid(row=2, column=0, columnspan=3, sticky=W+E)
        self.tampilan.grid(row=3, column=0, columnspan=3, sticky=W+E)
        self.canvas.pack()

    def menghitung_bmi(self):
        try:
            tinggi = float(self.entry_tinggi.get()) / 100
            berat = float(self.entry_berat.get())
            bmi = berat / (tinggi ** 2)
            result = f"Indeks BMI: {bmi:.2f}\n"
            if bmi < 18.5:
                result += "Berat Badan Kurang"
            elif 18.5 <= bmi < 24.9:
                result += "Berat Badan Normal"
            elif 25 <= bmi < 29.9:
                result += "Berat Badan Berlebih"
            else:
                result += "Obesitas"
        except ValueError:
            result = "Masukkan angka dengan benar."
        self.tampilan.delete(1.0, END)
        self.tampilan.insert(END, result)
        
        # Clear previous rectangle and draw a new one
        self.canvas.delete("all")
        if "Berat Badan Kurang" in result:
            color = "red"
        elif "Berat Badan Normal" in result:
            color = "green"
        elif "Berat Badan Berlebih" in result:
            color = "yellow"
        elif "Obesitas" in result:
            color = "red"
        else:
            color = "black"
        self.canvas.create_rectangle(50, 10, 350, 40, fill=color)

root = Tk()
kalkulator_bmi = BMI_Kalkulator(root)
root.mainloop()
