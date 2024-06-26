#================================================================ Soal 1
from tkinter import Tk, Label, Button, Entry, IntVar, END, W, E
class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")
        self.total = 0
        self.entered_number = 0
        self.total_label_text = IntVar()
        self.total_label_text.set(self.total)
        self.total_label = Label(master, textvariable=self.total_label_text)
        self.label = Label(master, text="Total:")
        vcmd = master.register(self.validate) # we have to wrap the command
        self.entry = Entry(master, validate="key", validatecommand=(vcmd, '%P'))
        self.add_button = Button(master, text="+", command=lambda: self.update("add"))
        self.subtract_button = Button(master, text="-", command=lambda: self.update("subtract"))
        self.reset_button = Button(master, text="Reset", command=lambda: self.update("reset"))
        # LAYOUT
        self.label.grid(row=0, column=0, sticky=W)
        self.total_label.grid(row=0, column=1, columnspan=2, sticky=E)
        self.entry.grid(row=1, column=0, columnspan=3, sticky=W+E)
        self.add_button.grid(row=2, column=0)
        self.subtract_button.grid(row=2, column=1)
        self.reset_button.grid(row=2, column=2, sticky=W+E)
    def validate(self, new_text):
        if not new_text: # the field is being cleared
            self.entered_number = 0
            return True
        try:
            self.entered_number = int(new_text)
            return True
        except ValueError:
            return False
    def update(self, method):
        if method == "add":
            self.total += self.entered_number
        elif method == "subtract":
            self.total -= self.entered_number
        else: # reset
            self.total = 0
            self.total_label_text.set(self.total)
            self.entry.delete(0, END)
 
root = Tk()
my_gui = Calculator(root)
root.mainloop()

#================================================================ Soal 2
from tkinter import Tk, Label, Button, Entry, IntVar, END, W, E

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")
        self.total = 0
        self.entered_number = 0
        self.total_label_text = IntVar()
        self.total_label_text.set(self.total)
        self.total_label = Label(master, textvariable=self.total_label_text)
        self.label = Label(master, text="Total:")
        vcmd = master.register(self.validate) # we have to wrap the command
        self.entry = Entry(master, validate="key", validatecommand=(vcmd, '%P'))
        self.add_button = Button(master, text="+", command=lambda: self.update("add"))
        self.subtract_button = Button(master, text="-", command=lambda: self.update("subtract"))
        self.reset_button = Button(master, text="Reset", command=lambda: self.update("reset"))
        self.multiplication_button = Button(master, text="x", command=lambda: self.update("multiply"))
        self.division_button = Button(master, text="/", command=lambda: self.update("divide"))
        
        # LAYOUT
        self.label.grid(row=0, column=0, sticky=W)
        self.total_label.grid(row=0, column=1, columnspan=2, sticky=E)
        self.entry.grid(row=1, column=0, columnspan=3, sticky=W+E)
        self.add_button.grid(row=2, column=0)
        self.subtract_button.grid(row=2, column=1)
        self.reset_button.grid(row=2, column=2, sticky=W+E)
        self.multiplication_button.grid(row=3, column=0, padx=5, pady=10)
        self.division_button.grid(row=3, column=1, padx=10, pady=10)

    def validate(self, new_text):
        if not new_text: # the field is being cleared
            self.entered_number = 0
            return True
        try:
            self.entered_number = int(new_text)
            return True
        except ValueError:
            return False

    def update(self, method):
        if method == "add":
            self.total += self.entered_number
        elif method == "subtract":
            self.total -= self.entered_number
        elif method == "multiply":
            self.total *= self.entered_number
        elif method == "divide":
            # Prevent division by zero
            if self.entered_number != 0:
                self.total /= self.entered_number
            else:
                self.total = 'Error'
        else: # reset
            self.total = 0
        
        self.total_label_text.set(self.total)
        self.entry.delete(0, END)

root = Tk()
my_gui = Calculator(root)
root.mainloop()

#================================================================ Soal 3
import tkinter as tk
from tkinter import messagebox

welcome_image = None

def verifikasi_identitas():
    if entry_username.get() == "uhuy" and entry_password.get() == "123":
        login_window.destroy()
        welcome_screen()
    else:
        messagebox.showerror("Masukin yang bener dong")

def welcome_screen():
    global welcome_image
    welcome_window = tk.Tk()
    welcome_window.geometry("668x374")  
    welcome_window.title("Selamat Datang")
    
    #memuat gambar
    welcome_image = tk.PhotoImage(file="D:\\Download\\4d93je.png") 
    label_image = tk.Label(welcome_window, image=welcome_image)
    label_image.pack()
    
    label_welcome = tk.Label(welcome_window, text="Selamat Datang!", font=("Arial", 16))
    label_welcome.pack(expand=True)
    
    welcome_window.mainloop()

#window utama
login_window = tk.Tk()
login_window.geometry("668x374")
login_window.title("Login")

#frame untuk form login
frame_login = tk.Frame(login_window)
frame_login.pack(padx= 50, pady=90)

#label dan entry untuk username
label_username = tk.Label(frame_login, text="Username:")
label_username.grid(row=0, column=0)
entry_username = tk.Entry(frame_login)
entry_username.grid(row=0, column=1)

#label dan entry untuk password
label_password = tk.Label(frame_login, text="Password:")
label_password.grid(row=1, column=0)
entry_password = tk.Entry(frame_login, show="*")
entry_password.grid(row=1, column=1)

#tombol login
button_login = tk.Button(login_window, text="Login", command=verifikasi_identitas)
button_login.pack(padx= 10, pady=0)

login_window.mainloop()
