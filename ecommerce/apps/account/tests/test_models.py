import pytest


def test_customer_str(customer):
    assert customer.__str__() == "user1"


def test_adminuser_str(adminuser):
    assert adminuser.__str__() == "admin_user"


def test_address_str(address):
    name = address.full_name
    assert address.__str__() == name + " Address"
