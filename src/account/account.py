class Account():
    def __init__(self, id):
        self.__id = id
        self.__balance = 0

    def __overdraft(self, amount):
        if amount > self.__balance:
            return True
        else:
            return False

    def get_id(self):
        return self.__id

    def get_balance(self):
        return self.__balance
    
    def deposit(self, amount):
        self.__balance += amount
        return self.__balance

    def withdrawl(self, amount):
        if self.__overdraft(amount):
            return(ValueError("Overdraft: Not enough funds to withdrawl!"))
        self.__balance -= amount
        return self.__balance

    def transfer(self, account, amount):
        if self.__overdraft(amount):
            return(ValueError("Overdraft: Not enough funds to transfer!"))
        self.__balance -= amount
        account.__balance += amount
        return self.__balance

    def interest(self, rate):
        self.__balance += self.__balance*rate