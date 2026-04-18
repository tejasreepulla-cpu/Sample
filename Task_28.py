# ATM program with functions:

def credit(amount):
    global balance
    if amount<=0:
        print("Please enter a positive amount.")
    else:
        balance+=amount
        print(f"${amount} credited to your account.")
def debit(amount):
    global balance
    if amount<=0:
        print("Please enter a positive amount.")
    elif amount>balance:
        print("Insufficient balance...")
    else:
        balance-=amount
        print(f"${amount} debited from your account.")
def balance_method():
    global balance
    print(f"Your current balance is: ${balance}")
def exit():
    print("Thank you for using the ATM. Goodbye!")
    
balance = 0
while True:
    print("\nATM Menu:")
    print("1. Credit")
    print("2. Debit")
    print("3. Balance")
    print("4. Exit")
    
    choice = int(input("Enter your choice (1-4): "))
    if choice == 1:
        amount = float(input("Enter amount to credit: "))
        credit(amount)
    elif choice == 2:
        amount = float(input("Enter amount to dedit: "))
        debit(amount)
    elif choice == 3:
        balance_method()
    elif choice == 4:
        exit()
    else:
        print("Invalid choice. Please try again.")