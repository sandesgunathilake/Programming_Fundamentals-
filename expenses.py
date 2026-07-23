def add_expense():
    expense_name = input("Enter expense name: ")
    
    amount = input("Enter expense amount: ")

    file = open("expenses.txt", "a")
    file.write(expense_name + "," + amount + "\n")
    file.close()

    Print("Expense added successfully")
    
