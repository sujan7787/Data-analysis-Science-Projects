import json

def register(username, pin):
    try:
        file = open("atm_credentials.txt", "r")
        content = file.read()
        file.close()
    except FileNotFoundError:
        content = ""
 
    credentials = content.split("-")
    for i in credentials:
        if i != "":
            dict_credentials = json.loads(i)
            if username in dict_credentials:
                print("Username already exists! Please choose another one.")
                return

    file = open("atm_credentials.txt", "a")
    dict_credentials = {username: pin}
    json_credentials = json.dumps(dict_credentials)
    file.write(json_credentials + "-")
    file.close()

    file = open("balance.txt", "a")
    dict_balance = {username: 0}
    json_balance = json.dumps(dict_balance)
    file.write(json_balance + "-")
    file.close()

    print("Registration successful!")


def login(username, pin):
    try:
        file = open("atm_credentials.txt", "r")
        content = file.read()
        file.close()
    except FileNotFoundError:
        print("No users registered yet.")
        return False

    credentials = content.split("-")
    for i in credentials:
        if i != "":
            dict_credentials = json.loads(i)
            if username in dict_credentials and dict_credentials[username] == pin:
                print("Login Successful.")
                return True
    print("Invalid username or password.")
    return False


def view_balance(username):
    file = open("balance.txt", "r")
    content = file.read()
    file.close()

    balance_data = content.split("-")
    for i in balance_data:
        if i != "":
            dict_balance = json.loads(i)
            if username in dict_balance:
                print("Your current balance is:", dict_balance[username])
                return


def add_balance(username):
    file = open("balance.txt", "r")
    content = file.read()
    file.close()

    balance_data = content.split("-")
    new_content = ""
    # balance_data = [{Ujjwal: 1000},{Ram: 500},{Shyam: 100},""]
    for i in balance_data:
        if i != "":
            dict_balance = json.loads(i)
            # username = Ram
            if username in dict_balance:
                amount = int(input("Enter the amount you want to add: "))
                # amount = 2000
                dict_balance[username] += amount # previous = 500, amount = 2000, dict_balance[username] = 500+2000 = 2500 
                print("Balance updated! New balance:", dict_balance[username])
            new_content += json.dumps(dict_balance) + "-"
            # new_content = {Ujjwal: 1000}-{Ram: 2500}-{Shyam:100}-

    file = open("balance.txt", "w")
    file.write(new_content)
    file.close()


def withdraw_balance(username):
    file = open("balance.txt", "r")
    content = file.read()
    file.close()

    balance_data = content.split("-")
    new_content = ""
    for i in balance_data:
        if i != "":
            dict_balance = json.loads(i)
            if username in dict_balance:
                amount = int(input("Enter the amount you want to withdraw: "))
                if amount > dict_balance[username]:
                    print("Insufficient funds!")
                else:
                    # {"Ujjwal":1000}-
                    # amount = 500
                    dict_balance[username] -= amount # dict_balance[username] = 1000-500 = 500
                    print("Withdrawal successful! New balance:", dict_balance[username])
            new_content += json.dumps(dict_balance) + "-"
            # {"Ujjwal":500}

    file = open("balance.txt", "w")
    file.write(new_content)
    file.close()


# ---------------- Main Program ----------------

while True:
    choice = input("\nDo you want to Register (r), Login (l), or Exit (e): ").lower()
    if choice == "r":
        username = input("Enter your username: ")
        pin = input("Enter your pin: ")
        register(username, pin)

    elif choice == "l":
        username = input("Enter your username: ")
        pin = input("Enter your pin: ")
        is_login = login(username, pin)
        if is_login:
            while True:
                print("\n--- ATM Menu ---")
                print("1. View Balance")
                print("2. Add Balance")
                print("3. Withdraw Balance")
                print("4. Logout")
                atm_task = input("Enter choice: ")

                if atm_task == "1":
                    view_balance(username)
                elif atm_task == "2":
                    add_balance(username)
                elif atm_task == "3":
                    withdraw_balance(username)
                elif atm_task == "4":
                    print("Logged out!")
                    break
                else:
                    print("Invalid choice.")
    elif choice == "e":
        print("Exiting ATM. Goodbye!")
        break
    else:
        print("Invalid option! Choose 'r', 'l', or 'e'.")
        
print("Thank you for using our system.")
