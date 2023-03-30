
# Written by Emin Ayyıldız

import tkinter as tk
from tkinter import messagebox


class Phonebook:
    def __init__(self, master):
        self.master = master
        master.title("*** PHONE BOOK *** Written by EMIN AYYILDIZ")
        master.geometry("450x250")
        master.resizable(width=False, height=False)
        master.configure(background='#add8e6')

        self.label_name = tk.Label(master, text="Name : ", font=("Arial", 12, "bold"), background='#add8e6')
        self.label_name.grid(row=1, column=0)

        self.entry_name = tk.Entry(master, justify="center", font=("Arial", 12, "bold"))
        self.entry_name.grid(row=1, column=1)

        self.label_surname = tk.Label(master, text="Surname : ", font=("Arial", 12, "bold"), background='#add8e6')
        self.label_surname.grid(row=2, column=0)

        self.entry_surname = tk.Entry(master, justify="center", font=("Arial", 12, "bold"))
        self.entry_surname.grid(row=2, column=1)

        self.label_phone_work = tk.Label(master, text="Phone Number Work :", font=("Arial", 12, "bold"),
                                         background='#add8e6')
        self.label_phone_work.grid(row=3, column=0)

        self.entry_phone_work = tk.Entry(master, justify="center", font=("Arial", 12, "bold"))
        self.entry_phone_work.grid(row=3, column=1)

        self.label_phone_home = tk.Label(master, text="Phone Number Home :", font=("Arial", 12, "bold"),
                                         background='#add8e6')
        self.label_phone_home.grid(row=4, column=0)

        self.entry_phone_home = tk.Entry(master, justify="center", font=("Arial", 12, "bold"))
        self.entry_phone_home.grid(row=4, column=1)

        self.button_add = tk.Button(master, text="Add Contact", command=self.add_contact, font=("Arial", 12, "bold"),
                                    background='orange')
        self.button_add.grid(row=5, column=0)

        self.button_list = tk.Button(master, text="List all Contact", command=self.list_contacts,
                                     font=("Arial", 12, "bold"), background='orange')
        self.button_list.grid(row=5, column=1)

        self.button_exit = tk.Button(master, text="Exit", command=master.quit, font=("Arial", 12, "bold"),
                                     background='orange')
        self.button_exit.grid(row=5, column=2)

    def add_contact(self):
        name = self.entry_name.get()
        surname = self.entry_surname.get()
        phone_work = self.entry_phone_work.get()
        phone_home = self.entry_phone_home.get()

        if not name or not surname or not phone_work or not phone_home:
            messagebox.showerror("ERROR", "Please fill in all fields...")
        else:

            contact = name + " " + surname + " - Work :  " + phone_work + " - Home : " + phone_home
            self.entry_name.delete(0, tk.END)
            self.entry_surname.delete(0, tk.END)
            self.entry_phone_work.delete(0, tk.END)
            self.entry_phone_home.delete(0, tk.END)
            with open("contacts.txt", "a") as f:
                f.write(contact + "\n")
            messagebox.showinfo("INFORMATION", "The contact has been successfully added.")


    def list_contacts(self):
        try:
            with open("contacts.txt", "r") as f:
                contacts = f.read()
                messagebox.showinfo("Persons", contacts)
        except FileNotFoundError:
            messagebox.showerror("ERROR", "The person was not found.")


root = tk.Tk()
my_phonebook = Phonebook(root)
root.mainloop()
