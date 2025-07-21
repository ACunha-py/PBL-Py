# Budget_Tracker_gui.py
import tkinter as tk
from tkinter import ttk
import Budget_Tracker as logic


class BudgetApp:
    def __init__(self, root):
        """ Start application window """
        self.root = root
        self.root.title("PBL: Budget Tracker")
        self.root.geometry("1280x800")

        self.transactions = logic.load_transactions()

        self.main_frame = ttk.Frame(self.root, padding="10")
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        self.create_widgets()
        self.populate_transactions_view()

    def create_widgets(self):
        """ Create widgets and arrange them """
        top_frame = ttk.Frame(self.main_frame)
        top_frame.pack(fill=tk.X, pady=10, side=tk.TOP)

        tree_frame = ttk.Frame(self.main_frame)
        tree_frame.pack(fill=tk.BOTH, expand=True, side=tk.TOP)

        title_label = ttk.Label(
            top_frame,
            text="Personal Budget Tracker",
            font=("Atkinson Hyperlegible Regular", 20, "bold")
        )
        title_label.pack()

        columns = ('ID', 'Date', 'Type', 'Category', 'Description', 'Amount')
        self.tree = ttk.Treeview(tree_frame, columns=columns, show='headings')

        self.tree.heading('ID', text='ID')
        self.tree.heading('Date', text='Date')
        self.tree.heading('Type', text='Type')
        self.tree.heading('Category', text='Category')
        self.tree.heading('Description', text='Description')
        self.tree.heading('Amount', text='Amount (€)')

        self.tree.column('ID', width=50, stretch=tk.NO)
        self.tree.column('Date', width=160, stretch=tk.NO)
        self.tree.column('Type', width=100, stretch=tk.NO)
        self.tree.column('Category', width=150)
        self.tree.column('Description', width=400)
        self.tree.column('Amount', width=120, anchor=tk.E)

        scrollbar = ttk.Scrollbar(tree_frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)

        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    def populate_transactions_view(self):
        """ Clears Treeview and fills it with current data """
        for item in self.tree.get_children():
            self.tree.delete(item)

        for i, transaction in enumerate(self.transactions):
            transaction_id = i + 1
            amount_str = f"{transaction['amount']:.2f}"
            category = transaction.get('category', 'N/A')

            self.tree.insert(
                '',
                tk.END,
                values=(transaction_id, transaction['date'], transaction['type'], category, transaction['description'],
                        amount_str)
            )




if __name__ == "__main__":
    root = tk.Tk()
    app = BudgetApp(root)
    root.mainloop()