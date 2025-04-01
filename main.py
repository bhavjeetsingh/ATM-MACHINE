def load_balance():
    with open("../../Desktop/balance.txt") as data:
        balance = float(data.read())
        if data == '':
            return 0 

    with open("../../Desktop/balance.txt", mode="w") as data:
        data.write(float(balance))
        
def show_balance(balance):
    print(f"Your balance is ${balance: .2f}")


def deposit():
    amount = float(input("Enter an amount to be deposited:"))
    if amount < 0:
        print("Invalid amount.")
        return 0
    else:
        return amount
def withdraw(balance):
    amount = float(input("Enter amount to be withdrawn:"))
    if amount <= 0:
        print("Invalid amount.")
        return 0
    elif amount > balance:
        print("Insufficient funds.")
        return 0
    else:
        return amount

def main():
    balance = 0 
    is_running = True

    while is_running:
        print("********************************")
        print("      Banking program         ")
        print("********************************")
        print("1.Show Balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("Exit")
        print("********************************")

        choice = (input("Enter your choice: (1-4): "))

        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            is_running = False
        else:
            print("********************************")
            print("Invalid choice. Please try again.")
            print("********************************")
    print("Thank you have a nice day!")
if __name__ == '__main__':
    main()