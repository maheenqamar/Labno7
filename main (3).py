import tkinter as tk
from tkinter import messagebox
import re
import pandas as pd



class FormApp:

  def __init__(self, master):
    self.master = master
    self.master.title("User Form")

    self.name_label = tk.Label(master, text="Name:")
    self.name_label.grid(row=0, column=0, sticky="w")
    self.name_entry = tk.Entry(master)
    self.name_entry.grid(row=0, column=1)

    self.email_label = tk.Label(master, text="Email:")
    self.email_label.grid(row=1, column=0, sticky="w")
    self.email_entry = tk.Entry(master)
    self.email_entry.grid(row=1, column=1)

    self.phone_label = tk.Label(master, text="Phone Number:")
    self.phone_label.grid(row=2, column=0, sticky="w")
    self.phone_entry = tk.Entry(master)
    self.phone_entry.grid(row=2, column=1)

    self.address_label = tk.Label(master, text="Address:")
    self.address_label.grid(row=3, column=0, sticky="w")
    self.address_entry = tk.Entry(master)
    self.address_entry.grid(row=3, column=1)

    self.job_label = tk.Label(master, text="Job Title:")
    self.job_label.grid(row=4, column=0, sticky="w")
    self.job_entry = tk.Entry(master)
    self.job_entry.grid(row=4, column=1)

    self.income_label = tk.Label(master, text="Income:")
    self.income_label.grid(row=5, column=0, sticky="w")
    self.income_entry = tk.Entry(master)
    self.income_entry.grid(row=5, column=1)

    self.submit_button = tk.Button(master,
                                   text="Submit",
                                   command=self.submit_form)
    self.submit_button.grid(row=6, columnspan=2)
    
   

  def submit_form(self):
    name = self.name_entry.get()
    email = self.email_entry.get()
    phone = self.phone_entry.get()
    address = self.address_entry.get()
    job_title = self.job_entry.get()
    income = self.income_entry.get()

    # Validation
    if len(name) < 3 or len(name) > 25:
      messagebox.showerror("Error",
                           "Name should be between 3 and 25 characters")
      return
    if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',
                    email):
      messagebox.showerror("Error", "Invalid email format")
      return
    if not re.match(r'^\+?92\d{10}$', phone):
      messagebox.showerror("Error", "Invalid Pakistani mobile number format")
      return
    if len(address) > 65:
      messagebox.showerror("Error", "Address should not exceed 65 characters")
      return
    if len(job_title) > 15:
      messagebox.showerror("Error",
                           "Job title should not exceed 15 characters")
      return
    if not re.match(r'^\$?[0-9]+(\.[0-9]{1,2})?/-$', income):
      messagebox.showerror("Error", "Invalid income format")
      return
      
  
      
    # Save to Excel
    data = {
        'Name': [name],
        'Email': [email],
        'Phone Number': [phone],
        'Address': [address],
        'Job Title': [job_title],
        'Income': [income]
    }
    df = pd.DataFrame(data)
    df.to_excel("user_data.xlsx", index=False)

    messagebox.showinfo("Success", "Form submitted successfully")
    self.master.destroy()


def main():
  root = tk.Tk()
  app = FormApp(root)
  root.mainloop()


if __name__ == "__main__":
  main()
