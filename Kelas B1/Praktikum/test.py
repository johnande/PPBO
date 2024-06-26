
# # # import tkinter as tk
# # # from tkinter import messagebox
# # # from PIL import Image, ImageTk

# # # # Memuat gambar untuk window pertama
# # # login_image = None

# # # def verify_credentials():
# # #     if entry_username.get() == "uhuy" and entry_password.get() == "123":
# # #         login_window.destroy()
# # #         welcome_screen()
# # #     else:
# # #         messagebox.showerror("Login Gagal", "Username atau Password salah!")

# # # def welcome_screen():
# # #     global welcome_image
# # #     welcome_window = tk.Tk()
# # #     welcome_window.geometry("668x374")  
# # #     welcome_window.title("Selamat Datang")
    
# # #     # Memuat gambar untuk welcome screen
# # #     welcome_image = ImageTk.PhotoImage(Image.open("D:\\Download\\4d93je.png"))
# # #     label_image = tk.Label(welcome_window, image=welcome_image)
# # #     label_image.pack()
    
# # #     label_welcome = tk.Label(welcome_window, text="Selamat Datang!", font=("Arial", 16))
# # #     label_welcome.pack(expand=True)
    
# # #     welcome_window.mainloop()

# # # # Window utama
# # # login_window = tk.Tk()
# # # login_window.geometry("668x374")
# # # login_window.title("Login")

# # # # Memuat gambar untuk window pertama
# # # login_image = ImageTk.PhotoImage(Image.open("D:\Download\LOGO FIX.png"))
# # # label_image_login = tk.Label(login_window, image=login_image)
# # # label_image_login.pack()

# # # # Frame untuk form login
# # # frame_login = tk.Frame(login_window)
# # # frame_login.pack(padx=50, pady=90)

# # # # Label dan entry untuk username
# # # label_username = tk.Label(frame_login, text="Username:")
# # # label_username.grid(row=0, column=0)
# # # entry_username = tk.Entry(frame_login)
# # # entry_username.grid(row=0, column=1)

# # # # Label dan entry untuk password
# # # label_password = tk.Label(frame_login, text="Password:")
# # # label_password.grid(row=1, column=0)
# # # entry_password = tk.Entry(frame_login, show="*")
# # # entry_password.grid(row=1, column=1)

# # # # Tombol login
# # # button_login = tk.Button(login_window, text="Login", command=verify_credentials)
# # # button_login.pack(padx=10, pady=0)

# # # login_window.mainloop()

# # import tkinter as tk
# # from tkinter import ttk
# # from tkinter import messagebox

# # def sign_up():
# #     sign_up_window = tk.Toplevel()
# #     sign_up_window.title("Sign Up")
# #     sign_up_window.geometry("300x200")

# #     # Frame untuk memasang semua komponen
# #     sign_up_frame = ttk.Frame(sign_up_window, padding="10")
# #     sign_up_frame.pack(fill=tk.BOTH, expand=True)

# #     # Label dan Entry untuk nama
# #     nama_label = ttk.Label(sign_up_frame, text="Nama:")
# #     nama_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
# #     nama_entry = ttk.Entry(sign_up_frame)
# #     nama_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

# #     # Label dan Entry untuk email
# #     email_label = ttk.Label(sign_up_frame, text="Email:")
# #     email_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
# #     email_entry = ttk.Entry(sign_up_frame)
# #     email_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")

# #     # Label dan Entry untuk password
# #     password_label = ttk.Label(sign_up_frame, text="Password:")
# #     password_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
# #     password_entry = ttk.Entry(sign_up_frame, show="*")
# #     password_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")

# #     # Button untuk sign up
# #     sign_up_button = ttk.Button(sign_up_frame, text="Sign Up")
# #     sign_up_button.grid(row=3, column=0, columnspan=2, padx=5, pady=10)

# # def login():
# #     login_window = tk.Toplevel()
# #     login_window.title("Login")
# #     login_window.geometry("300x200")

# #     # Frame untuk memasang semua komponen
# #     login_frame = ttk.Frame(login_window, padding="10")
# #     login_frame.pack(fill=tk.BOTH, expand=True)

# #     # Label dan Entry untuk email
# #     email_label = ttk.Label(login_frame, text="Email:")
# #     email_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
# #     email_entry = ttk.Entry(login_frame)
# #     email_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

# #     # Label dan Entry untuk password
# #     password_label = ttk.Label(login_frame, text="Password:")
# #     password_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
# #     password_entry = ttk.Entry(login_frame, show="*")
# #     password_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")

# #     # Button untuk login
# #     login_button = ttk.Button(login_frame, text="Login")
# #     login_button.grid(row=2, column=0, columnspan=2, padx=5, pady=10)

# # # Create main window
# # window = tk.Tk()
# # window.title("Sistem Input UKT (SIPUT)")
# # window.geometry("300x400")

# # # Create logo
# # logo_label = ttk.Label(window, text="SIPUT", font=("Arial", 24))
# # logo_label.pack(pady=20)

# # # Create welcome message


# from kivy.app import App
# from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.label import Label
# from kivy.uix.button import Button
# from kivy.uix.image import Image
# from kivy.core.window import Window

# Window.size = (360, 640)

# class SIPUTApp(App):
#     def build(self):
#         main_layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
#         # Menambahkan Logo
#         logo = Image(source='/mnt/data/image.png')
#         main_layout.add_widget(logo)
        
#         # Menambahkan Label Selamat Datang
#         welcome_label = Label(
#             text='[b]Welcome to\nSistem Input UKT (SIPUT)[/b]',
#             markup=True,
#             font_size='24sp',
#             halign='center',
#             valign='middle'
#         )
#         main_layout.add_widget(welcome_label)
        
#         # Menambahkan Deskripsi
#         description_label = Label(
#             text='Sistem Input UKT (SIPUT) merupakan sistem terintegrasi yang digunakan untuk melakukan pembayaran UKT mahasiswa dengan metode yang sederhana dan mudah digunakan oleh seluruh kalangan civitas academica',
#             font_size='16sp',
#             halign='center',
#             valign='middle',
#             text_size=(320, None)
#         )
#         main_layout.add_widget(description_label)
        
#         # Menambahkan Spasi
#         main_layout.add_widget(Label(size_hint_y=None, height=50))
        
#         # Menambahkan Tombol Sign Up
#         sign_up_button = Button(
#             text='Sign Up',
#             size_hint=(None, None),
#             size=(200, 50),
#             pos_hint={'center_x': 0.5}
#         )
#         main_layout.add_widget(sign_up_button)
        
#         # Menambahkan Tombol Login
#         login_button = Button(
#             text='Login',
#             size_hint=(None, None),
#             size=(200, 50),
#             pos_hint={'center_x': 0.5}
#         )
#         main_layout.add_widget(login_button)
        
#         return main_layout

# if __name__ == '__main__':
#     SIPUTApp().run()


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
