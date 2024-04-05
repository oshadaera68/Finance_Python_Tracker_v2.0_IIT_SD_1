# finance tracker v2.0: using dictionaries + json
# importing json module
import json

# initialize the empty directory
transactions = []


# file handling
# load the file
def load_transactions():
    global transactions
    try:
        with open("trans.json", "r") as file:
            json.load(file)
    except FileNotFoundError:
        print("No transactions. Please try again")
    except json.decoder.JSONDecodeError:
        transactions = []


# save the transactions
def save_transactions():
    # write the data in the json file
    with open("trans.json", "w") as file:
        json.dump(transactions, file)


def read_bulk_transactions_from_file(filename):
    # Open and read the file, then parse each line to add to the transactions dictionary
    pass


# Feature implementations
def add_transaction():
    enter_choice = input("Transaction Completed. Do you want to add the another Transaction? [Y/N]:")
    if enter_choice == "y" or enter_choice == "Y":
        add_transaction()
    elif enter_choice == "n" or enter_choice == "N":
        main_menu()
    else:
        print("Invalid Value. Please Try Again!!")


def view_transactions():
    pass


def update_transaction():
    enter_choice = input("Transaction Completed. Do you want to add the another Transaction? [Y/N]:")
    if enter_choice == "y" or enter_choice == "Y":
        add_transaction()
    elif enter_choice == "n" or enter_choice == "N":
        main_menu()
    else:
        print("Invalid Value. Please Try Again!!")


def delete_transaction():
    enter_choice = input("Transaction Completed. Do you want to add the another Transaction? [Y/N]:")
    if enter_choice == "y" or enter_choice == "Y":
        add_transaction()
    elif enter_choice == "n" or enter_choice == "N":
        main_menu()
    else:
        print("Invalid Value. Please Try Again!!")


def display_summary():
    pass


def main_menu():
    # load all transactions in the json file
    load_transactions()
    while True:
        print("-----------------------------------------")
        print("|\t\t Personal Finance Tracker \t\t|")
        print("-----------------------------------------")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Update Transaction")
        print("4. Delete Transaction")
        print("5. Display Summary")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_transaction()
        elif choice == '2':
            view_transactions()
        elif choice == '3':
            update_transaction()
        elif choice == '4':
            delete_transaction()
        elif choice == '5':
            display_summary()
        elif choice == '6':
            exit_the_program()
        else:
            print("Invalid choice. Please try again.")


def exit_the_program():
    exit_choice = input("Did you want to exit the System? [Y/N]: ")
    if exit_choice == "y" or exit_choice == "Y":
        print("Program Exited")
        exit()
    elif exit_choice == "n" or exit_choice == "N":
        main_menu()
    else:
        print("Invalid Input.")
        exit(0)


# runnable main constructor
if __name__ == "__main__":
    main_menu()
