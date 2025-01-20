class UserAccount():
    # lastTransaction = ''

    def __init__(self, account_number, pin, balance):
        self.account_number = account_number
        self.pin = pin
        self.balance = balance
        # self.lastTransaction = lastTransaction

    def __str__(self):
        return f"This is account number: {self.account_number} of balance: {self.balance}"

    def checkPin(self, account_number, pin):
        if self.account_number == account_number:
            return True
        if self.pin != pin:
            return False

        return False

    def getBalance(self):
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return False
        self.lastTransaction = f"Balance was KES {
            self.balance}. Withdrew KES {amount}."
        self.balance -= amount

        return True

    def getLastTransaction(self):
        if self.lastTransaction != '':
            return self.lastTransaction

        return "No transactions"
