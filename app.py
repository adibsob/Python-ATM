from banking_pkg import account


def atm_menu(name):
    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")


print("          === Automated Teller Machine ===          ")
while True:
    name = input("Enter name to register: ")
    if len(name) > 10:
        print("The maximum name length is 10 characters.")
    elif len(name) == 0:
        print("You must enter a name.")
    else:
        break

while True:
    pin = input("Enter PIN: ")
    if len(pin) > 4 or len(pin) < 4:
        print("PIN must contain 4 numbers")
    else:
        break

balance = 0
print(name, "has been registered with a starting balance of $" + str(balance))


"""
Log in the user, or deny if PIN is invalid
"""
while True:
    print("          === Automated Teller Machine ===          ")
    print("LOGIN")
    name_to_validate = input("Enter name: ")
    pin_to_validate = input("Enter PIN: ")
    if name_to_validate == name and pin_to_validate == pin:
        print("Login successful!\n")
        break
    print("Invalid credentials!\n")


"""
Displays ATM menu and responds to user choice
"""
while True:
    atm_menu(name)
    option = input("Choose an option: ")
    if option == "1":               # balance
        account.show_balance(balance)
    elif option == "2":             # deposit
        balance = account.deposit(balance)
        account.show_balance(balance)
    elif option == "3":             # withdraw
        balance = account.withdraw(balance)
        account.show_balance(balance)
    else:                           # logout
        account.logout(name)
        break
