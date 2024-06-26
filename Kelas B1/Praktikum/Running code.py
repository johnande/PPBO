from tkinter import Tk, Label, Entry, Button, Frame, StringVar, END

class CashierSystem:
    def __init__(self, master):
        self.master = master
        master.title("Sistem Kasir")

        #Frame untuk input produk dan harga
        self.product_frame = Frame(master)
        self.product_frame.pack()

        self.product_label = Label(self.product_frame, text="Produk:")
        self.product_label.grid(row=0, column=0)

        self.product_entry = Entry(self.product_frame)
        self.product_entry.grid(row=0, column=1)

        self.price_label = Label(self.product_frame, text="Harga:")
        self.price_label.grid(row=1, column=0)

        self.price_entry = Entry(self.product_frame)
        self.price_entry.grid(row=1, column=1)

        #Frame untuk tombol
        self.action_frame = Frame(master)
        self.action_frame.pack()

        self.add_button = Button(self.action_frame, text="Tambah", command=self.add_item)
        self.add_button.grid(row=0, column=0)

        self.print_button = Button(self.action_frame, text="Cetak Bill", command=self.print_bill)
        self.print_button.grid(row=0, column=1, padx= 10, pady= 10)

        self.reset_button = Button(self.action_frame, text="Reset", command=self.reset_entries)
        self.reset_button.grid(row=0, column=2)

        #Frame untuk output bill
        self.bill_frame = Frame(master)
        self.bill_frame.pack()

        self.bill_label = Label(self.bill_frame, text="Bill:")
        self.bill_label.pack()

        self.bill_text = StringVar()
        self.bill_output = Label(self.bill_frame, textvariable=self.bill_text, bg='white', width=40, height=10)
        self.bill_output.pack()

        self.items = []

    def add_item(self):
        product = self.product_entry.get()
        price = self.price_entry.get()
        if product and price:
            self.items.append((product, price))
            self.product_entry.delete(0, END)
            self.price_entry.delete(0, END)
            self.update_bill()

    def update_bill(self):
        bill_content = "\n".join(f"{product}: {price}" for product, price in self.items)
        self.bill_text.set(bill_content)

    def print_bill(self):
        #Ini akan mencetak bill ke layar, bisa disesuaikan untuk mencetak ke printer
        print("Bill:")
        for product, price in self.items:
            print(f"{product}: {price}")
        print("Terima kasih telah berbelanja!")

    def reset_entries(self):
        self.product_entry.delete(0, END)
        self.price_entry.delete(0, END)
        self.items.clear()
        self.bill_text.set("")

root = Tk()
my_cashier = CashierSystem(root)
root.mainloop()
