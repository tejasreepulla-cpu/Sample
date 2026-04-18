# ATM program using OOPs
# class ATM():
#     def __init__(self,bank,location,branch,balance=1000):
#         self.bank=bank
#         self.location=location
#         self.branch=branch
#         self.balance=balance
#     def credit(self,amount):
#         if amount<=0:
#             print("Please enter a positive amount.")
#         else:
#             self.balance+=amount
#             print(f"${amount} credited to your account from {self.bank}.")
#     def debit(self,amount):
#         if amount<=0:
#             print("Please enter a positive amount.")
#         elif amount>self.balance:
#             print("Insufficient balance...")
#         else:
#             self.balance-=amount
#             print(f"${amount} debited from your account from {self.bank}.")
#     def balance_method(self):
#         print(f"Your current balance is: ${self.balance}")
#     def exit(self):
#         print("Thank you for using the ATM. Goodbye!")

# sbi=ATM("SBI","Hyderabad","Miryalaguda",15000)
# print(sbi.balance)
# print(sbi.location)
# print(sbi.branch)
# print(sbi.bank)
# sbi.credit(15000)
# sbi.balance_method()
# sbi.debit(5000)
# sbi.balance_method()
# sbi.exit()

# while True:
#     print("\nATM Menu:")
#     print("1. Credit")
#     print("2. Debit")
#     print("3. Balance")
#     print("4. Exit")
#     choice = int(input("Enter your choice (1-4): "))
#     if choice == 1:
#         amount = float(input("Enter amount to credit: "))
#         sbi.credit(amount)
#     elif choice == 2:
#         amount = float(input("Enter amount to dedit: "))
#         sbi.debit(amount)
#     elif choice == 3:
#         sbi.balance_method()
#     elif choice == 4:
#         sbi.exit()
#     else:
#         print("Invalid choice. Please try again.")

# ATM Program using Inheritance concept:
class ATM():
    def __init__(self,bank,location,branch,balance=1000):
        self.bank=bank
        self.location=location
        self.branch=branch
        self.balance=balance
    def credit(self,amount):
        if amount<=0:
            print("Please enter a positive amount.")
        else:
            self.balance+=amount
            print(f"${amount} credited to your account from {self.bank}.")
    def debit(self,amount):
        if amount<=0:
            print("Please enter a positive amount.")
        elif amount>self.balance:
            print("Insufficient balance...")
        else:
            self.balance-=amount
            print(f"${amount} debited from your account from {self.bank}.")
class ATM_machine(ATM):
    def balance_method(self):
        print(f"Your current balance is: ${self.balance}")
    def exit(self):
        print("Thank you for using the ATM. Goodbye!")

sbi=ATM_machine("SBI","Hyderabad","Miryalaguda",15000)
print(sbi.balance)
print(sbi.location)
print(sbi.branch)
print(sbi.bank)
sbi.credit(15000)
sbi.balance_method()
sbi.debit(5000)
sbi.balance_method()
sbi.exit()

hdfc=ATM_machine("HDFC","Bangalore","Majestic",10000)
print(hdfc.balance)
print(hdfc.location)
print(hdfc.branch)
print(hdfc.bank)
hdfc.credit(10000)
hdfc.balance_method()
hdfc.debit(7000)
hdfc.balance_method()
hdfc.exit()

while True:
    print("\nATM Menu:")
    print("1. Credit")
    print("2. Debit")
    print("3. Balance")
    print("4. Exit")
    choice = int(input("Enter your choice (1-4): "))
    if choice == 1:
        amount = float(input("Enter amount to credit: "))
        sbi.credit(amount)
    elif choice == 2:
        amount = float(input("Enter amount to dedit: "))
        sbi.debit(amount)
    elif choice == 3:
        sbi.balance_method()
    elif choice == 4:
        sbi.exit()
    else:
        print("Invalid choice. Please try again.")
        
        
