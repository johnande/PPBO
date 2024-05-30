from tkinter import Tk, Label, Button, Entry, Canvas, Text, Frame, W, E, END, simpledialog

class GuestBookApp:
    def __init__(self, master):
        self.master = master
        master.title("Buku Tamu Digital")

        # Frame for input fields
        self.input_frame = Frame(master)
        self.input_frame.grid(row=0, column=0, padx=10, pady=10)

        # Name Label and Entry
        self.name_label = Label(self.input_frame, text="Nama:")
        self.name_label.grid(row=0, column=0, sticky=W)
        self.name_entry = Entry(self.input_frame)
        self.name_entry.grid(row=0, column=1, sticky=E)

        # Message Label and Entry
        self.message_label = Label(self.input_frame, text="Pesan:")
        self.message_label.grid(row=1, column=0, sticky=W)
        self.message_entry = Entry(self.input_frame)
        self.message_entry.grid(row=1, column=1, sticky=E)

        # Submit Button
        self.submit_button = Button(self.input_frame, text="Submit", command=self.add_guest)
        self.submit_button.grid(row=2, columnspan=2, pady=5)

        # Create Canvas for displaying guest book entries
        self.canvas = Canvas(master, width=400, height=200, bg='lightgrey')
        self.canvas.grid(row=1, column=0, padx=10, pady=10)

        # Create Text widget for displaying guest book entries
        self.entries_text = Text(master, height=10, width=50)
        self.entries_text.grid(row=2, column=0, padx=10, pady=5)

        # Edit Button
        self.edit_button = Button(master, text="Edit Entry", command=self.edit_entry)
        self.edit_button.grid(row=3, column=0, pady=5)

        # List to store guest entries
        self.entries = []

    def add_guest(self):
        # Get the name and message from the entry fields
        name = self.name_entry.get()
        message = self.message_entry.get()

        # Add the new entry to the entries list
        self.entries.append((name, message))

        # Update the displayed entries
        self.update_entries_display()

        # Clear the entry fields after submission
        self.name_entry.delete(0, END)
        self.message_entry.delete(0, END)

    def update_entries_display(self):
        # Clear the text widget
        self.entries_text.delete(1.0, END)

        # Display all entries in the text widget
        for idx, (name, message) in enumerate(self.entries):
            self.entries_text.insert(END, f"{idx+1}. Name: {name}\n   Message: {message}\n\n")

    def edit_entry(self):
        # Prompt the user for the entry number to edit
        entry_number = simpledialog.askinteger("Edit Entry", "Enter entry number to edit:")

        if entry_number is not None and 1 <= entry_number <= len(self.entries):
            name, message = self.entries[entry_number - 1]

            # Prompt the user for new name and message
            new_name = simpledialog.askstring("Edit Name", "Enter new name:", initialvalue=name)
            new_message = simpledialog.askstring("Edit Message", "Enter new message:", initialvalue=message)

            if new_name is not None and new_message is not None:
                # Update the entry with the new name and message
                self.entries[entry_number - 1] = (new_name, new_message)

                # Update the displayed entries
                self.update_entries_display()

root = Tk()
app = GuestBookApp(root)
root.mainloop()
