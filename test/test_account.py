import bank.src.account.account as account

import random
import time

def test_create():
    savings = account.Account(100)
    assert savings.get_balance() == 0

def test_deposit():
    savings = account.Account(100)

    random.seed(int(time.time()))
    add = round(random.uniform(20.0, 100.0), 2)

    assert savings.deposit(add) == add

def test_withdrawl():
    savings = account.Account(100)

    random.seed(int(time.time()))
    add = round(random.uniform(20.0, 100.0), 2)
    remove = round(random.uniform(0.0, add), 2)

    savings.deposit(add)
    final = add - remove

    assert savings.withdrawl(remove) == final

def test_overdraft():
    savings = account.Account(100)

    random.seed(int(time.time()))
    add = round(random.uniform(20.0, 100.0), 2)
    remove = round(random.uniform(add, 200.0), 2)

    savings.deposit(add)

    assert type(savings.withdrawl(remove)) == ValueError