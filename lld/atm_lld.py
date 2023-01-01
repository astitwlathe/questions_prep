"""
How to solve LLD:
1. Clarify the requirements
2. Hash out the primary use cases
3. Identify key objects
4. Identify Operations supported by Objects
5. Identify Interactions between objects

The main components of the ATM that will affect interactions between the ATM and its users are:
1. Card reader: to read the users' ATM cards.
2. Keypad: to enter information into the ATM, e.g., PIN cards.
3. ScreenL to display messages to the user.
4. Cash dispenser: for dispensing cash.
5. Deposit slot: For users to deposit cash or checks.
6. Prinetr: For printing receipts.
7. Communication/Network Infrastructure: It is assumed that ATM has a cummunication infrastructure to communicate 
   with the bank upon any upon any transaction or activity.


1. Balance inquiry: To see the amount of funds in each account.
2. Deposit cash: To deposit cash.
3. Deposit check: To deposit checks.
4. Withdraw cash: To withdraw money from their checking account.
5. Transfer funds: To transfer funds to another accounts.

--- Use Cases
Here are the actors of the ATM system and their use cases:
Operator: The operator will be responsible for the following operations:
1. Turning ATM ON/OFF using the designated Key-Switch.
2. Refilling ATM with cash.
3. Refilling ATM's printer with receipts.
4. Refilling ATM't printer with INK
5. Take out deposited cash and checks.

Customer: ATM customer can perform the following operations:
1. Balance inquiry: The user can view his/her ccount balance.
2. Cash withdrawal: The user can withdraw a certai amount of cash.
3. Deposit funds: The user can deposit cash or checks.
4. Transfer funds: The user can transfer funds to other accounts.

Bank Manager: The Bank Manager can perform the following operations:
1. Generate a report to check total deposits.
2. Generate a report to check total withdrawals. 
3. Print total depostis/withdrawal reports.
4. Checks the remaining cash in ATM.

--- Class Diagram
Here are the main classes of ATM System:
* ATM * CashReader * CashDispenser * Keypad * Screen * Printer * DepositSlot * Bank * Account * Customer
* Card * Transaction

"""

# Enums and Constants: Here are the required enums, data types, and constants:

from abc import ABC
from enum import Enum
from re import I


class TransactionType(Enum):
    BALANCE_INQUIRY, DEPOSIT_CASH, DEPOSIT_CHECK, WITHDRAW, TRANSFER = 1, 2, 3, 4, 5

class CustomerStatus(Enum):
    ACTIVE, BLOCKED, BANNED, COMPROMISED, ARCHIVED, CLOSED, UNKNOWN = 1, 2 , 3, 4, 5, 6, 7

class Address:
    def __init__(self, street, city, state, zip_code, country):
        self.__street = street
        self._city = city
        self.__state = state
        self.__zip_code = zip_code
        self__country = country

# Customer, Card, and Account: "Customer" encapsulates the ATM user, "card" the ATM card, and "Account" can be of 2 types: checking and savings:

class Customer:
    def __init__(self, name, address, email, phone, status):
        self.__name = name
        self.__address = address
        self.__email = email
        self.__phone = phone
        self.__status = status
        self.__card = Card()
        self.__account = Account()

        def make_transaction(self, transaction):
            pass

        def get_billing_address(self):
            pass

class Card:
    def __init__(self, number, customer_name, expiry, pin):
        self.__card_number = number
        self.__customer_name = customer_name
        self.__card_expiry = expiry
        self.__pin = pin

    def get_billing_address(self):
        pass

class Account:
    def __init__(self, account_number):
        self.__account_number = account_number
        self.__total_balance = 0.0
        self.__available_balance = 0.0

    def get_available_balance(self):
        return self.__available_balance

class SavingAccount(Account):
    def __init__(self, Account, withdraw_limit):
        self.__withdraw_limit = withdraw_limit

class CheckingAccount(Account):
    def __init__(self, debit_card_number):
        self.__debit_card_number = debit_card_number

# Bank, ATM, CashDispenser, Keypad, Screen, Printer, and DepositSlot: ATM will have different components like keypad, screen, etc.

class Bank:
    def __init__(self, name, bank_code):
        self.__name - name
        self.__bank_code = bank_code

    def get_bank_code(self):
        return self.__bank_code
    
    def add_atm(self, atm):
        pass


class ATM:
    def __init__(self, id, location):
        self.__atm_id = id
        self.__location = location
        self.__cash_dispenser = CashDispenser()
        self.__keypad = Keypad()
        self.__screen = Screen()
        self.__printer = Printer()
        self.__check_deposit = CheckDeposit()
        self.__cash_deposit = CashDeposit()

        def authenticate_user(self):
            pass

        def make_transaction(self, customer, transaction):
            pass

class CashDispenser:
    def __init__(self):
        self.__total_five_dollar_bills = 0
        self.__total_twenty_dollar_bills = 0
    
    def dispense_cash(self, amount):
        pass
    def can_dispense_cash(self):
        pass

class Keypad:
    def get_input(self):
        pass

class Screen:
    def show_message(self, message):
        pass

    def get_input(self):
        pass

class Printer:
    def print_receipt(self, transaction):
        pass

class DepositSlot(ABC):
    def __init__(self):
        self.__total_amount = 0.0

    def get_total_amount(self):
        return self.__total_amount

class CheckDepositSlot(DepositSlot):
    def get_check_amount(self):
        pass

class CashDepositSlot(DepositSlot):
    def receive_dollar_bill(self):
        pass

# Transaction and its subclasses: Customers can perform different transactions in the ATM, these class encapsulate them:

from abc import ABC, abstractmethod

class Transaction(ABC):
    def __init__(self, id, creation_date, status):
        self.__transaction_id = id
        self.__creation_date = creation_date
        self.__status = status

    def make_transaction(self):
        pass

class BalanceInquiry(Transaction):
    def __init__(self, account_id):
        self.__account_id = account_id

        def get_account_id(self):
            return self.__account_id

class Deposit(Transaction):
    def __init__(self, amount):
        self.__amount = amount

    def get_amount(self):
        return self.__amount

class CheckDeposit(Deposit):
    def __init__(self, check_number, bank_code):
        self.__check_number = check_number
        self.__bank_code = bank_code

class CashDeposit(Deposit):
    def __init__(self, cash_deposit_limit):
        self.__cash_deposit_limit = cash_deposit_limit

class Withdraw(Transaction):
    def __init__(self, amount):
        self.__amount = amount

    def get_amount(self):
        return self.__amount


class Transfer(Transaction):
    def __init__(self, destination_account_number):
        self.__destination_account_number = destination_account_number

    def get_destination_account(self):
        return self.__destination_account_number
