# finance tracker v2.0: using dictionaries + json
# importing json module
import json

# initialize the empty directory
transactions = {}


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
        transactions = {}

    # transactions.update()


# save the transactions
def save_transactions():
    # write the data in the json file
    with open("trans.json", "w") as file:
        json.dump(transactions, file)
        file.write('\n')


def date_validation(date_text):
    try:
        year, month, day = map(int, date_text.split('-'))  # Split the date string and convert parts to integers
        if month < 1 or month > 12 or day < 1 or day > 31:
            return False  # Invalid month or day
        # Check for months with 30 days
        if month in [4, 6, 9, 11] and day > 30:
            return False
        # Check for February
        if month == 2:
            if day > 29:
                return False  # February cannot have more than 29 days
            if day == 29 and not (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
                return False  # Not a leap year
        return True
    except ValueError:
        return False


def read_bulk_transactions_from_file(file_name):
    # try:
    #     filename = input("Enter the filename to read bulk transactions from: ")
    #     global transactions
    #     with open(filename, 'r') as file:
    #         transactions = json.load(file)
    # except FileNotFoundError:
    #     print("Not Found")
    # except json.JSONDecodeError:
    #     print("Try again..")
    pass


# Feature implementations
def add_transaction():
    print("---------------------------------")
    print("|\t\t Add Transaction \t\t|")
    print("---------------------------------")
    # inputting data with validation
    while True:
        insert_type = input("Enter the type: ")
        if not insert_type:
            print("Please Type it!!")
            continue
        else:
            insert_amount = int(input("Enter the amount: "))
            if insert_amount <= 0:
                print("Enter the valid amount. Don't type the negative amount.")
                continue
            else:
                insert_date = input("Enter the date: ")
                if not date_validation(insert_date):
                    print("Enter the valid date.")
                    continue
                break

    # adding the transactions
    add = {"amount": insert_amount, "date": insert_date}

    # check the adding transactions for in the transactions dictionary
    if insert_type in transactions:
        transactions[insert_type].append(add)
    else:
        transactions[insert_type] = [add]
    save_transactions()

    enter_choice = input("Transaction Completed. Do you want to add the another Transaction? [Y/N]:")
    if enter_choice == "y" or enter_choice == "Y":
        add_transaction()
    elif enter_choice == "n" or enter_choice == "N":
        main_menu()
    else:
        print("Invalid Value. Please Try Again!!")


# viewing all datas
def view_transactions():
    print("---------------------------------")
    print("|\t\t View Transactions \t\t|")
    print("---------------------------------")


# update
def update_transaction():
    print("-------------------------------------")
    print("|\t\t Update Transactions \t\t|")
    print("-------------------------------------")

    print("All Transactions List")
    print(str(transactions) + "\n")

    update_type = input("Enter the Type: ")
    if update_type != transactions.keys() and len(transactions[update_type]) > 0:
        print("\nwhat do you want to the update?")
        print("1. Amount")
        print("2. Date")
        print("3. Cancel Update")
        choice = input("Enter the choice to update: ")

        while True:
            if choice == "1":
                while True:
                    try:
                        print(f"current amount: {transactions[update_type][0]['amount']}")
                        amount = int(input("Enter the new Amount: "))
                        if amount < 0:
                            print("Amount must be a positive integer.")
                        else:
                            break
                    except ValueError:
                        print("Invalid Number. Please type the valid number")

                transactions[update_type][0]['amount'] = amount
                print(amount)
                break

            elif choice == "2":
                print(f"current amount: {transactions[update_type][0]['date']}")
                date = input("Enter the new date (YYYY-MM-DD): ")
                if not date_validation(date):
                    print("Invalid Date. Please Try again.")
                else:
                    transactions[update_type][0]['date'] = date
                    print(date)
                    break

            elif choice == "3":
                print("Update is canceled.")
                break
            else:
                print("Invalid Choice. Try Again.")
                break

    save_transactions()

    enter_choice = input("Transaction Completed. Do you want to update the another Transaction? [Y/N]:")
    if enter_choice == "y" or enter_choice == "Y":
        update_transaction()
    elif enter_choice == "n" or enter_choice == "N":
        main_menu()
    else:
        print("Invalid Value. Please Try Again!!")


# delete
def delete_transaction():
    print("-------------------------------------")
    print("|\t\t Delete Transactions \t\t|")
    print("-------------------------------------")

    print("All Transactions List")
    print(str(transactions) + "\n")

    delete_type = input("Enter the type for delete: ")





    enter_choice = input("Transaction Completed. Do you want to delete the another Transaction? [Y/N]:")
    if enter_choice == "y" or enter_choice == "Y":
        delete_transaction()
    elif enter_choice == "n" or enter_choice == "N":
        main_menu()
    else:
        print("Invalid Value. Please Try Again!!")


# showing summary
def display_summary():
    print("---------------------------------")
    print("|\t\t Display Summary \t\t|")
    print("---------------------------------")

    pass


# main menu
def main_menu():
    # load all transactions in the json file
    load_transactions()
    while True:
        print("-----------------------------------------")
        print("|\t\t Personal Finance Tracker \t\t|")
        print("-----------------------------------------")
        print("1. Add Transaction")
        print("2. View Transaction")
        print("3. Update Transaction")
        print("4. Delete Transaction")
        print("5. Display Summary")
        print("6. Read Bulk Transactions")
        print("7. Exit")
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
        elif choice == '7':
            exit_the_program()
        else:
            print("Invalid choice. Please try again.")


# exiting program
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
