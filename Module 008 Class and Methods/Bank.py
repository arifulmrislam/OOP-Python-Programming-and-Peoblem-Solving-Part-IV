class Bank:
    def __init__(self, balance):
        self.balance = balance
        self.min_withdraw = 100
        self.max_withdraw = 10000
        
    def get_balance(self):
        return self.balance

    def withdraw(self, amount):
        if amount < self.min_withdraw:
            return 'no money for you'
        elif amount > self.max_withdraw:
            return f'you crossed max limit: {self.max_withdraw}'
        elif amount > self.balance:
            return 'You are broke !! No money for you'
        else:
            self.balance = self.balance - amount
            return f'Here is you money: {amount}'
    def deposit(self,amount):
        self.balance = self.balance + amount

my_bank = Bank(8000)
reply = my_bank.withdraw(500)
print(reply)
print(f'Current balance: {my_bank.get_balance()}')
my_bank.deposit(5000)
print(my_bank.get_balance())