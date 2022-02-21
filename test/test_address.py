import bank.src.address.address as address

def test_create():
    street = "123 Main Street"
    city = "Springfield"
    state = "VA"
    zip = 12345

    addr = address.Address(street, city, state, zip)
    
    assert addr.street == street
    assert addr.city == city
    assert addr.state == state
    assert addr.zip == zip