class Bank():
    def __init__(self):
        self.customers = []
        self.accounts = []

    def add_customer(self, customer):
        self.customers.append(customer)

    def compoud_interest(self, rate):
        for account in self.accounts:
            account.interest(rate)