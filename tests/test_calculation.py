from app.calculations import add
import pytest


# @pytest.fixture
# def zero_bank():
#     return BankAccount()

# @pytest.fixture
# def bank_account(50):
#     return BankAccount(50)

@pytest.mark.parametrize("num1, num2, expected", [
    (3, 2, 5),
    (3, 7, 10),
    (2, 2, 4),
])
def test_add(num1, num2, expected):
    print("testing add fucntion")
    assert add(num1, num2) == expected


def test_set_initial_deposit(zero_bank):
    with pytest.raises(Exception):
        assert zero_bank.balance == 0
