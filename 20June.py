class BankAccount:
    def __init__(self, account_number, account_holder_name, balance=0.0):
        self.account_number=account_number
        self.account_holder_name=account_holder_name
        self.balance=balance

    def deposit(self, amount):
        self.balance+=amount
        print(f'Deposited {amount} into account number {self.account_number}')

    def withdraw(self, amount):
        if self.balance>=amount:
            self.balance-=amount
            print(f'Withdraw {amount} from account {self.account_number}')
        else:
            print('Insufficient Balance.')

    def check_balance(self):
        print(f'Current balance: {self.balance}')

account = BankAccount(input("Enter account number: "),input("Enter account holder name: "))
account.deposit(1000 )
account.withdraw(500)
account.check_balance()


