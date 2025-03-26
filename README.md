# ExpenseTracker - Expense Tracker

## Project Description

ExpenseTracker is a desktop application for tracking income and expenses, written in Python using the PySide6 framework. Data is stored in an SQLite database, providing a convenient way to manage financial transactions.

## Features

- ✅ **Add, edit, and delete transactions** (income and expenses).
- 💰 **Calculate total balance** as well as separate expense categories (🚗 Auto, 🛒 Groceries, 🎉 Entertainment, 🏠 Other).
- 📊 **Display all transactions** in an easy-to-use table with sorting capabilities.
- 🗄️ **Use an SQLite database** for data storage with automatic table creation if it does not exist.
- 🖥️ **Graphical user interface** implemented with PySide6.

## Technologies

- 🐍 **Programming Language**: Python
- 🖼️ **GUI Framework**: PySide6
- 🗄️ **Database**: SQLite

## Installation and Launch

### 1. 🔽 Clone the Repository

```sh
git clone https://github.com/iDeash123/Expenses.git
cd Expenses
```

### 2. 📦 Install Dependencies

Before running the application, install PySide6:

```sh
pip install PySide6
```

### 3. 🚀 Run the Application

```sh
python main.py
```

## Project Structure

```
Expenses/
│── main.py              # 🏁 Main application file
│── connection.py        # 🗄️ Module for working with the SQLite database
│── new_transaction.py   # ➕ Interface for adding/editing transactions
│── ui_main.py           # 🎨 Generated UI file for the main window
│── expense_db.db        # 🛢️ Database file (created automatically)
└── README.md            # 📖 Project description
```

## Main Classes and Their Functions

### `Data`

Class for working with the SQLite database:

- 🔌 `create_connection()` – establishes a connection to the database and creates the table if necessary.
- ➕ `add_new_transaction_query()` – adds a new expense or income record.
- ✏️ `update_transaction_query()` – edits an existing record.
- ❌ `delete_transaction_query()` – deletes a record and resets the auto-increment ID if needed.
- 📊 Methods for calculating total sums (`total_balance()`, `total_income()`, `total_outcome()`, etc.).

### `ExpenseTracker`

Main application window:

- 📋 `view_data()` – displays transactions in the table.
- 🔄 `reload_data()` – updates balance indicators.
- 🆕 `open_new_transaction_window()` – opens a window for adding/editing records.
- ➕ `add_new_transaction()` – adds a new transaction to the database.
- ✏️ `edit_current_transaction()` – edits the selected transaction.
- ❌ `delete_current_transaction()` – deletes a transaction.

## Possible Improvements

- 🏷️ Add customizable expense categories.
- 📤 Implement data export to CSV or Excel.
- 📈 Include graphs for visualizing expenses and income.

### If you have suggestions for improving the project or found a bug – feel free to create an issue or a pull request! 🚀

###
