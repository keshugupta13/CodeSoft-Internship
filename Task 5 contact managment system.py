import tkinter as tk
from tkinter import messagebox

# Sample data structure to store contacts
contacts = []

def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()
    if name and phone:
        contacts.append({"name": name, "phone": phone, "email": email, "address": address})
        clear_entries()
        update_contact_list()
    else:
        messagebox.showerror("Error", "Name and Phone are required fields.")

def update_contact_list():
    contact_listbox.delete(0, tk.END)
    for contact in contacts:
        contact_listbox.insert(tk.END, f"{contact['name']} - {contact['phone']}")

def search_contact():
    query = search_entry.get().lower()
    contact_listbox.delete(0, tk.END)
    for contact in contacts:
        if query in contact['name'].lower() or query in contact['phone']:
            contact_listbox.insert(tk.END, f"{contact['name']} - {contact['phone']}")

def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)
    search_entry.delete(0, tk.END)

def delete_contact():
    selected_index = contact_listbox.curselection()
    if selected_index:
        index = int(selected_index[0])
        contacts.pop(index)
        update_contact_list()
        clear_entries()
    else:
        messagebox.showerror("Error", "Please select a contact to delete.")

def update_contact():
    selected_index = contact_listbox.curselection()
    if selected_index:
        index = int(selected_index[0])
        name = name_entry.get()
        phone = phone_entry.get()
        email = email_entry.get()
        address = address_entry.get()
        if name and phone:
            contacts[index] = {"name": name, "phone": phone, "email": email, "address": address}
            update_contact_list()
            clear_entries()
        else:
            messagebox.showerror("Error", "Name and Phone are required fields.")
    else:
        messagebox.showerror("Error", "Please select a contact to update.")

# Create the main window
app = tk.Tk()
app.title("Contact Management System")

# Create and configure GUI elements
name_label = tk.Label(app, text="Name:")
name_label.pack()
name_entry = tk.Entry(app)
name_entry.pack()

phone_label = tk.Label(app, text="Phone:")
phone_label.pack()
phone_entry = tk.Entry(app)
phone_entry.pack()

email_label = tk.Label(app, text="Email:")
email_label.pack()
email_entry = tk.Entry(app)
email_entry.pack()

address_label = tk.Label(app, text="Address:")
address_label.pack()
address_entry = tk.Entry(app)
address_entry.pack()

add_button = tk.Button(app, text="Add Contact", command=add_contact)
add_button.pack()

search_label = tk.Label(app, text="Search:")
search_label.pack()
search_entry = tk.Entry(app)
search_entry.pack()

search_button = tk.Button(app, text="Search Contact", command=search_contact)
search_button.pack()

contact_listbox = tk.Listbox(app, selectmode=tk.SINGLE)
contact_listbox.pack()

update_button = tk.Button(app, text="Update Contact", command=update_contact)
update_button.pack()

delete_button = tk.Button(app, text="Delete Contact", command=delete_contact)
delete_button.pack()

clear_entries()

app.mainloop()

