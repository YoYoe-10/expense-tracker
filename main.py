import json
import os
DATA_FILE = "expenses.json"

def load_expenses():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return []

def save_expenses():
    with open(DATA_FILE, "w") as file:
        json.dump(expenses, file, indent=4)





def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    amount = float(input("Enter amount: $"))
    category = input("Enter category (e.g., Food, Transport, etc.): ")
    description = input("Enter description (optional): ")

    expense = {
        "date": date,
        "amount": amount,
        "category": category,
        "description": description
    }

    expenses.append(expense)
    save_expenses()
    print("Expense added successfully!\n")

def view_expenses():
    if not expenses:
        print("No expenses recorded yet.\n")
        return

    print("Date         |  Amount  | Category     | Description")
    print("-" * 50)
    for e in expenses:
        print(f"{e['date']:12} | ${e['amount']:7.2f} | {e['category']:<12} | {e['description']}")
        print()

def total_expenses() :
    total = sum(e['amount'] for e in expenses)
    print(f"Total spent: ${total:.2f}\n")

def filter_by_category():
    cat = input("Enter category to filter: ").lower()
    filtered = [e for e in expenses if e['category'].lower() == cat]

    if not filtered:
        print("No expenses found in this category.\n")
        return
    print(f"Expenses in category '{cat}':")
    for e in filtered:
        print(f"{e['date']} | ${e['amount']:.2f} | {e['description']}")
    print()

from collections import defaultdict

def monthly_summary():
    summary = defaultdict(float)
    for e in expenses:
        month = e['date'][:7]
        summary[month] += e['amount']

    print("Monthly Summary:")
    for month, total in sorted(summary.items()):
        print(f"{month}: ${total:.2f}")
    print()

def sort_expenses():
    print("Sort by:")
    print("1. Amount")
    print("2. Date")
    choice = input("Choose option: ")

    if choice == "1":
        sorted_exp = sorted(expenses, key=lambda e: e['amount'], reverse=True)
    elif choice == "2":
        sorted_exp = sorted(expenses, key=lambda e: e['date'])
    else:
        print("Invalid choice.\n")
        return
    for e in sorted_exp:
        print(f"{e['date']} | ${e['amount']:.2f} | {e['category']} | {e['description']}")
    print()

from colorama import Fore, Style, init
init()
def view_expenses_colored():
    for e in expenses:
        color = Fore.GREEN if e['category'].lower() == "food" else Fore.YELLOW
        print(color + f"{e['date']} | ${e['amount']:.2f} | {e['category']} | {e['description']}" + Style.RESET_ALL)

import csv
def export_to_csv():
    with open("expenses.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["date", "amount", "category", "description"])
        writer.writeheader()
        writer.writerows(expenses)
    print("Expenses exported to expenses.csv\n")

def main():
    while True:
        print("=== Expense Tracker Menu ===")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Total Spent")
        print("4. Filter by Category")
        print("5. Monthly Summary")
        print("6. Sort Expenses")
        print("7. Export to CSV")
        print("8. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_expenses()
        elif choice == "4":
            filter_by_category()
        elif choice == "5":
            monthly_summary()
        elif choice == "6":
            sort_expenses()
        elif choice == "7":
            export_to_csv()
        elif choice == "8":
            print("Goodbye!")
            break
        else:
            print("Invalid input. Try again.\n")


expenses = load_expenses()
main()
