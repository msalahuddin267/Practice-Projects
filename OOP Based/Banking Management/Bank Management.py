class Bank:
    bank_balance = 0
    total_loan = 0
    can_loan = True
    
    def __init__(self, name) -> None:
        self.name = name
    
class Admin(Bank):
    def __init__(self, name, email, password) -> None:
        super().__init__(name)
        self.name = name
        self.email = email
        self.password = password

    def check_bank_available_balance(self):
        print(f'Current Bank Balance: {Bank.bank_balance}')

    def check_total_loan_amount(self):
        print(f'Total Loan Amount: {Bank.total_loan}')

    def loan_off(self):
        Bank.can_loan = False

    def loan_on(self):
        Bank.can_loan = True

class User(Bank):
    def __init__(self, name, email, password, amount) -> None:
        super().__init__(name)
        self.name = name
        self.email = email
        self.password = password
        self.user_balance = amount
        Bank.bank_balance += amount
        self.id = None
        self.loan = 0
        self.transaction_history = []
        self.transaction_history.append(f'Initial deposit amount: {amount}')


    def deposite_amount(self, amount):
        if amount > 0:
            self.user_balance += amount
            Bank.bank_balance += amount
            self.transaction_history.append(f'Deposit amount: {amount}')
            
        else:
            print('Plese give possitive amount.')

    def withdraw_amount(self, amount):
        if self.user_balance >= amount <= Bank.bank_balance:
            self.user_balance -= amount
            Bank.bank_balance -= amount
            self.transaction_history.append(f'Withdraw amount: {amount}')

        elif Bank.bank_balance < amount:
            print('Not withdraw right now. Because bank is bankrupt.')

        else:
            print("You have not Sufficiant Balance.")

    def check_available_balace(self):
        print(f'Your Current Balance : {self.user_balance}')

    def transfer_amount(self, reciver, amount):
        if amount <= self.user_balance:
            self.user_balance -= amount
            reciver.user_balance -= amount
            self.transaction_history.append(f'Transfer amount: {amount} to {reciver.name} account')
            reciver.transaction_history.append(f'Received amount: {amount} from {self.name} account')

        else:
            print(f'You have not sufficiant balance')

    def take_loan(self, amount):
        max_loan = self.user_balance * 2
        if Bank.can_loan == True:
            if self.loan > 0:
                print('You have already take loan from bank.')

            elif amount > max_loan:
                print(f'You cross your loan limit. You can loan maximum {max_loan}')

            elif amount > Bank.bank_balance:
                print(f'Bank has not sufficiant balance now. You can loan maximum {Bank.bank_balance}')

            else:
                self.loan = amount
                self.user_balance += amount
                Bank.bank_balance -= amount
                Bank.total_loan += amount
                self.transaction_history.append(f'Take Loan: {amount} from bank.')

        else:
            print('Bank Loan Service Off now.')


    def show_transaction_history(self):
        print(f'------- {self.name} Statement --------')
        for x in self.transaction_history:
            print(x)

# ----------- Main -------------

abul = User('Abul', 'abul@gmail.com', '1234', 1000)
babul = User('babul', 'babul@gmail.com', '5678', 2000)

abul.deposite_amount(1500)
abul.take_loan(1500)

babul.deposite_amount(500)
babul.take_loan(200)

abul.show_transaction_history()
babul.show_transaction_history()

admin = Admin('admin', 'admin@email.com', 'adm1234')

admin.check_bank_available_balance()
admin.check_total_loan_amount()

admin.loan_off()
abul.take_loan(2000)




