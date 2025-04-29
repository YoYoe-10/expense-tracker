import tkinter as tk
from tkinter import ttk
import json
import os

DATA_FILE = "expenses.json"

def update_total_label():
    total = sum(e['amount'] for e in expenses)
    total_label.config(text=f"Total Spent: ${total:.2f}")

def load_expenses():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return []

def save_expenses():
    with open(DATA_FILE, "w") as file:
        json.dump(expenses, file, indent=4)

def add_expense_gui():
    date = date_entry.get()
    amount = amount_entry.get()
    category = category_entry.get()
    description = description_entry.get()

    try:
        amount = float(amount)
    except ValueError:
        return

    expense = {
        "date": date,
        "amount": amount,
        "category": category,
        "description": description
    }

    expenses.append(expense)
    save_expenses()
    update_expense_table()
    update_total_label()
    clear_fields()

def clear_fields():
    date_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)
    category_entry.delete(0, tk.END)
    description_entry.delete(0, tk.END)

def update_expense_table():
    for row in tree.get_children():
        tree.delete(row)
    for e in expenses:
        tree.insert("", tk.END, values=(e['date'], f"${e['amount']:.2f}", e['category'], e['description']))

# Load data
expenses = load_expenses()

# GUI window
root = tk.Tk()
root.title("Expense Tracker")

# Input form
tk.Label(root, text="Date (YYYY-MM-DD):").grid(row=0, column=0)
date_entry = tk.Entry(root)
date_entry.grid(row=0, column=1)

tk.Label(root, text="Amount:").grid(row=1, column=0)
amount_entry = tk.Entry(root)
amount_entry.grid(row=1, column=1)

tk.Label(root, text="Category:").grid(row=2, column=0)
category_entry = tk.Entry(root)
category_entry.grid(row=2, column=1)

tk.Label(root, text="Description:").grid(row=3, column=0)
description_entry = tk.Entry(root)
description_entry.grid(row=3, column=1)

tk.Button(root, text="Add Expense", command=add_expense_gui).grid(row=4, column=0, columnspan=2, pady=10)

# Table display
columns = ("Date", "Amount", "Category", "Description")
tree = ttk.Treeview(root, columns=columns, show="headings")
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=120)
tree.grid(row=5, column=0, columnspan=2, padx=10, pady=10)
total_label = tk.Label(root, text="Total Spent: $0.00", font=("Arial", 12, "bold"))
total_label.grid(row=6, column=0, columnspan=2, pady=(0, 10))

update_expense_table()
update_total_label()

root.mainloop()