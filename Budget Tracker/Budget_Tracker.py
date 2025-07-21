# budget_tracker.py
import json
import datetime

DATA_FILE = "budget_data.json"


def load_transactions():
    """Loads transactions from the JSON file."""
    try:
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_transactions():
    """Saves the current list of transactions to the JSON file."""
    with open(DATA_FILE, 'w') as file:
        json.dump(transactions, file, indent=4)


transactions = load_transactions()


def add_income():
    """Adds a new income and saves all transactions."""
    print("---- ADD INCOME ----")
    try:
        amount = float(input("Enter the income amount: "))
        description = input("Enter the description: (Ex.: 'Paycheck')")
        transaction = {
            "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
            "type": "income",
            "amount": amount,
            "description": description
        }
        transactions.append(transaction)
        save_transactions()
        print("✅ Income added successfully!")
    except ValueError:
        print("❌ Invalid amount. Please enter a number.")


def add_expense():
    """Adds a new expense and saves all transactions."""
    print("---- ADD EXPENSE ----")
    try:
        amount = float(input("Enter the expense amount: "))
        category = input("Enter the expense category: (Ex.: 'Living Expenses') ")
        description = input("Enter the expense description: ")
        transaction = {
            "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
            "type": "expense",
            "amount": amount,
            "category": category,
            "description": description
        }
        transactions.append(transaction)
        save_transactions()
        print("✅ Expense added successfully!")
    except ValueError:
        print("❌ Invalid amount. Please enter a number.")


def view_transactions():
    """Displays all recorded transactions with an ID."""
    print("\n---- All transactions ----")
    if not transactions:
        print("No transactions found!")
        return
    for i, transaction in enumerate(transactions):
        transaction_id = i + 1
        if transaction["type"] == "income":
            print(
                f"#{transaction_id}: [{transaction['date']}] ➕ Income: €{transaction['amount']:.2f}; ({transaction['description']})")
        else:
            print(
                f"#{transaction_id}: [{transaction['date']}] ➖ Expense: €{transaction['amount']:.2f}; [{transaction['category']}]; ({transaction['description']})")


def edit_transaction():
    """Edits an existing transaction selected by the user."""
    print("\n---- Edit Transaction ----")
    view_transactions()
    if not transactions:
        return

    try:
        id_to_edit = int(input("Enter the ID of the transaction to edit: "))
        index_to_edit = id_to_edit - 1

        if not (0 <= index_to_edit < len(transactions)):
            print("❌ Invalid ID. Please try again.")
            return

        transaction = transactions[index_to_edit]

        print("\nEnter new details. Press Enter to keep the current value.")

        current_amount = transaction['amount']
        new_amount_str = input(f"Enter new amount (current: {current_amount}): ")
        if new_amount_str:
            try:
                transaction['amount'] = float(new_amount_str)
            except ValueError:
                print("❌ Invalid amount. Keeping the current value.")

        current_description = transaction['description']
        new_description = input(f"Enter new description (current: '{current_description}'): ")
        if new_description:
            transaction['description'] = new_description

        if transaction['type'] == 'expense':
            current_category = transaction['category']
            new_category = input(f"Enter new category (current: '{current_category}'): ")
            if new_category:
                transaction['category'] = new_category

        save_transactions()
        print("✅ Transaction updated successfully!")

    except ValueError:
        print("❌ Invalid input. Please enter a number for the ID.")


def delete_transaction():
    """Deletes a transaction selected by the user."""
    print("\n---- Delete Transaction ----")
    view_transactions()
    if not transactions:
        return
    try:
        id_to_delete = int(input("Enter the ID of the transaction to delete: "))
        index_to_delete = id_to_delete - 1
        if 0 <= index_to_delete < len(transactions):
            transactions.pop(index_to_delete)
            save_transactions()
            print("✅ Transaction deleted successfully!")
        else:
            print("❌ Invalid ID. Please try again.")
    except ValueError:
        print("❌ Invalid input. Please enter a number.")


def calculate_balance():
    """Calculates and displays the total balance."""
    total_income = 0
    total_expenses = 0
    for transaction in transactions:
        if transaction["type"] == "income":
            total_income += transaction["amount"]
        else:
            total_expenses += transaction["amount"]
    balance = total_income - total_expenses
    print("\n---- Current Balance ----")
    print(f"Total income: €{total_income:.2f}")
    print(f"Total expenses: €{total_expenses:.2f}")
    print(f"Net Balance: €{balance:.2f}")


def view_summary():
    """Displays a summary of expenses by category."""
    print("\n---- Expenses by category ----")
    category_totals = {}
    for transaction in transactions:
        if transaction["type"] == "expense":
            category = transaction["category"]
            amount = transaction["amount"]
            category_totals[category] = category_totals.get(category, 0) + amount
    if not category_totals:
        print("No expenses to summarize yet.")
        return
    for category, total in category_totals.items():
        print(f" - {category}: €{total:.2f}")


def main():
    """Main Application loop."""
    while True:
        print("\n---- Budget Tracker Menu ----")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View All Transactions")
        print("4. Edit a Transaction")
        print("5. Delete a Transaction")
        print("6. Show Current Balance")
        print("7. View summary by category")
        print("8. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_income()
        elif choice == '2':
            add_expense()
        elif choice == '3':
            view_transactions()
        elif choice == '4':
            edit_transaction()
        elif choice == '5':
            delete_transaction()
        elif choice == '6':
            calculate_balance()
        elif choice == '7':
            view_summary()
        elif choice == '8':
            print("Thank you for using Budget Tracker. Bye 👋")
            break
        else:
            print("❌ Please enter a valid choice.")


if __name__ == "__main__":
    main()