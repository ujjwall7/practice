from random import randint




class Bank:
    def __init__(self) -> None:
        self.account = randint(10000,999999)
        self.full_name = input("Enter the name : ")
        self.balance = 0
        self.phone_number = int(input("Enter the phone number : "))

    def show_info(self):
        print(f'Account number : {self.account}')
        print(f'Full name : {self.full_name}')
        print(f'Phone number : {self.phone_number}')
        print(f'Balance : {self.balance}\n')
        
    def show_balance(self):
        print(f'Full name : {self.full_name}')
        print(f'Account number : {self.account}')
        print(f'Current Balance : {self.balance}')

    def withdraw(self):
        amount = int(input("Enter the withdraw amount : "))
        if amount > self.balance:
            print(f'Full name : {self.full_name}')
            print(f'Account number : {self.account}')
            print("Insufficient Balance")
            print()
        else:
            self.balance = self.balance - amount
            print(f'Full name : {self.full_name}')
            print(f'Phone number : {self.phone_number}')
            print(f'Balance : {self.balance}\n')
    
    def deposit(self):
        amount = int(input("Enter amount to deposit : "))
        self.balance = self.balance + amount
        print()
        print(f'Full name : {self.full_name}')
        print(f'Phone number : {self.phone_number}')
        print(f'Balance : {self.balance}\n')

# b1 = Bank()
# b1.show_balance()
# b1.deposit()
# b1.show_balance()
# b1.withdraw()
# b1.show_balance()

# #------obj 1----------
# x = Bank()
# banks = []
# banks.append(x)
# print(banks)

# print()

# #------obj 2----------
# y = Bank()
# banks.append(y)
# print(banks)

# print()

# banks[0].show_balance()
# banks[0].deposit()
# banks[0].show_balance()
# banks[0].withdraw()
# banks[0].show_balance()


banks = []
def check_account_exists(acc_no:int):
    global banks
    for obj in banks:
        if obj.account==acc_no:
            return obj

    return None


while True:
    print()
    print("1. create account")
    print("2. Show All banks details")
    print("3. Deposit Amount")
    print("4. Withdraw Amount")
    print("5. Transfer")
    print("6. Exit")
    print()
    choice = int(input("Enter the choice : "))
    if choice==1:
        obj = Bank()
        banks.append(obj)
    elif choice==2:
        if len(banks)==0:
            print("No account hab been created yet\n")
        else:
            for accounts in banks:
                accounts.show_info()
    elif choice==3:
        if len(banks)==0:
            print("No account hab been created yet\n")
        else:
            acc_no = int(input("Enter account number to deposit : "))

            for obj in banks:
                if obj.account == acc_no:
                    obj.deposit()
                    break
                else:
                   print("\nAccount Number not valid! plese try again")
    elif choice==4:
        if len(banks)==0:
            print("No account hab been created yet\n")
        else:
           acc_no = int(input("Enter account number to withdraw : "))
           
           for obj in banks: 
               if obj.account == acc_no:
                    obj.withdraw()
                    break
               else:
                   print("Account Number not valid! plese try again")
    elif choice==5:
        from_acc_no = int(input("Enter account number from which you want to transfer = "))   
        to_acc_no = int(input("Enter account number to which you want to transfer = "))   

        from_acc_obj =  check_account_exists(from_acc_no)
        to_acc_obj =  check_account_exists(to_acc_no)
        if from_acc_obj != None and to_acc_no != None:
            transfer_amount = int(input("Enter Transfer Amount = "))
            if from_acc_obj.balance < transfer_amount:
                print("Insufficient Balance")
            else:
                from_acc_obj.balance = from_acc_obj.balance - transfer_amount
                to_acc_obj.balance = to_acc_obj.balance + transfer_amount
        else:
            print("\nAccount Does Not Exists!")
    elif choice==6:
        break   
    else:
        print("Invalid choice\n")

















