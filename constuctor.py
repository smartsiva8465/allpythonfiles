class Banking:
    def __init__(self,name,account_number,balance=0):
        self.name=name
        self.account_number=account_number
        self.balance=balance
        print('holder name:',self.name)
        print('account number:',self.account_number)
        print('balance:',self.balance)
        print('\n')
    def deposit(self,amount):
        if amount >0:
            self.balance =self.balance + amount
            print(amount)
        else:
            print(' deposited amount must be greater')
    def withdraw(self,amount):
        if 0< amount <=self.balance:
            self.balance = self.balance - amount
            print(amount)
        else:
            print('insufficient balance')
    def display_balance(self):
        print(self.balance)
acc=Banking('siva',97654)
acc.deposit(20000)
acc.withdraw(16600)
acc.display_balance()


