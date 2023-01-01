"""
SOLID 
S: Single Responsibility Principle
O: Open for extension, closed for modification
L: Liskov Substitution Principle
I: Instance Segregation Principle
D: Depenedency Inversion Principle

Nouns: Users, product, search, cart, address, order, payment, track

Actors
* Admin, * Guest, * Member, * System

Top use cases of the Onilne Shopping System
1. Add/update products; whenever a product is added or modified, we will update the catalog.
2. Search for products by their name or category.
3. Add/remove product items in the shopping cart.
4. Check-out to buy product items in the shopping cart.
5. Make a payment to place an order.
6. Add a new product category.
7. Send notifications to members with shipment updates.

Class Diagram
* Account * Guest * Catalog * ProductCategory * Product * ProductReview * ShoppingCart * Item * Order * OrderLog * ShipmentLog
* Notification * Payment

"""

# Enums, data types, and constants: Here are the required enums, datatypes, and constants:

from enum import Enum
import datetime

class Address:
    def __init__(self, street, city, state, zip_code, country):
        self.__street = street
        self.__city = city
        self.__state = state
        self.__zip_code = zip_code
        self.__country = country

class OrderStatus(Enum):
    UNSHIPPED, PENDING, SHIPPED, COMPLETED, CANCELLED, REFUND_APPLIED = 1, 2, 3, 4, 5, 6

class AccountStatus(Enum):
    ACTIVE, BLOCKED, BANNED, COMPROMISED, ARCHIVED, UNKNOWN = 1, 2, 3, 4, 5, 6

class ShipmentStatus(Enum):
    PENDING, SHIPPED, DELIVERED, ON_HOLD  = 1, 2, 3, 4

class PaymentStatus(Enum):
    UNPAID, PENDING, COMPLETED, FILLED, DECLINED, CANCELLED, ABANDONED, SETTLING, SETTLED, REFUNDED = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

# Account, Customer, Admin, and Guest: These classes represent different pope that intercat with out system.

class Account:
    def __init__(self, user_name, password, name, email, phone, shipping_address, status=AccountStatus):
        self.__user_name = user_name
        self.__password = password
        self.__name = name
        self.__email = email
        self.__phone = phone
        self.__shipping_address = shipping_address
        self.__status = status.ACTIVE
        self.__credit_cards = []
        self.__bank_accounts = []

    def add_product(self, product):
        pass

    def add_productReview(self, review):
        pass

    def reset_password(self):
        pass

from abc import ABC, abstractmethod

class Customer(ABC):
    def __init__(self, cart, order):
        self.__cart = cart
        self.__order = order

    def get_shopping_cart(self):
        return self.__cart
    
    def add_item_to_cart(self, item):
        pass

    def remove_item_from_cart(self, item):
        pass

class Guest(Customer):
    def register_account(self):
        pass

class Member(Customer):
    def __init__(self, account):
        self.__account = account
    
    def place_order(self, order):
        pass

# ProductCategory Product, and ProductReview: Here are the classes related to a product:

class ProductCategory:
    def __init__(self, rating, review, reviewer):
        self.__rating = rating
        self.__review = review
        self.__reviewer = reviewer


class ProductReview:
    def __init__(self, rating, review, reviewer):
        self.__rating  = rating
        self.__review = review    
        self.__reviewer = reviewer

class Product:
    def __init__(self, id, name, description, price, category, seller_account):
        self.__product_id = id
        self.__name = name
        self.__description = description
        self.__price = price
        self.__category = category
        self.__available_item_count = 0
    
    def update_price(self, new_price):
        pass
# ShopingCart, Item, Order, and OrderLog

class Item:
    def __init__(self, id, quantity, price):
        self.__product_id = id
        self.__quantity = quantity
        self.__price = price 

    def update_quantity(self, quantity):
        pass

class ShoppingCart:
    def __init__(self):
        self.__items = []

    def add_iterm(self, item):
        pass
    
    def remove_item(self, item):
        pass

    def update_item_quantity(slef, item, quantity):
        pass

    def get_items(self):
        return self.__items
        
    def checkout(self):
        pass

class OrderLog:
    def __init__(self, order_number, status=OrderStatus.PENDING):
        self.__order_number = order_number
        self.__creation_date = datetime.date.today() 
        self.__status = status

class Order:
    def __init__(self, order_number, status=OrderStatus.PENDING):
        self.__order_number = order_number
        self.__status = status
        self.__order_date = datetime.date.today()
        self.__order_log = []

        def send_for_shipment(self):
            pass

        def make_payment(self, payment):
            pass

        def add_order_log(self, order_log):
            pass

# Shipment, ShipmentLog, and Notification: After successfully placing an order, a shipment record will be created:

    
