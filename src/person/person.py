class Person():
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.__account_ids = []

    def add_account(self, account_id):
        self.__account_ids.append(account_id)

    def remove_account(self, account_id):
        if account_id in self.__account_ids:
            self.__account_ids.remove(account_id)
            return True
        else:
            return ValueError("Account %s not found for %s" % (account_id, self.name))