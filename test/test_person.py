import bank.src.person.person as person

def test_valid_remove():
    client = person.Person("Jane Do", "123 ABC St")
    client.add_account(50)

    assert client.remove_account(50) == True

def test_invalid_remove():
    client = person.Person("John Do", "456 DEF St")
    client.add_account(100)

    assert type(client.remove_account(200)) == ValueError