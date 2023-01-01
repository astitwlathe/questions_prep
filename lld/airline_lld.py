"""
How to solve LLD .....
1. Requirements study.
2. Identify actors
Customer, Admin, Front Desk Officer, Pilot/Crew, System
3. Identify Use cases
* Search Flights
* Create/Modify/View reservation
* Assign seats to passengers
* Make payment for a reservation
* Update flight schedule
* Assign pilots and crew

4. Select class names
System
* Airline * Airport * Aircraft * Flight * FlightInstance * WeeklySchedule and CustomSchedule * FlightReservation
* Itinerary * FlightSeat * Payment * Notification

5. Write code
"""


from abc import ABC, abstractmethod
from enum import Enum, auto
from typing import List, Set, Dict

# Enums and Constants
class FlightStatus(Enum):
    ACTIVE, SCHEDULED, DELAYED, DEPARTED, LANDED, IN_AIR, ARRIVED, CANCELLED, DIVERTED, UNKNOWN = [auto() for _ in range(10)]

class PaymentStatus(Enum):
    UNPAID, PENDING, COMPLETED, FILLED, DECLINED, CANCELLED, ABANDONED, SETTLING, SETTLED, REFUNDED = [auto() for _ in range(10)]

class ReservationStatus(Enum):
    REQUESTED, PENDING, CONFIRMED, CHECKED_IN, CANCELLED, ABANDONED = [auto() for _ in range(6)]

class SeatClass(Enum):
    ECONOMY, ECONOMY_PLUS, PREFERRED_ECONOY, BUSINESS, FIRST_CLASS  = 1, 2, 3, 4, 5

class SeatType(Enum):
    REGULAR, ACCESSIBLE, EMERGENCY_EXIT, EXTRA_LEG_ROOM = 1, 2, 3, 4

class AccountStatus(Enum):
    ACTIVE, CLOSED, CANCELED, BLACKLISTED, BLOCKED = 1, 2, 3, 4, 5

class Address:
    def __init__(self, street, city, state, zip_code, country):
        self.__street_address:str = street
        self.__cityLstr = city
        self.__state:str = state
        self.__zip_code:str = zip_code
        self.__country:str = country


# Account, Person, Customer and Passenger
class Account:
    def __init__(self, id, password, status=AccountStatus.ACTIVE):
        self.__id:str = id
        self.__password:str = password
        self.__status:AccountStatus = status
    def reset_password(self):
        None

class Person(ABC):
    def __init__(self, name, address, email, phone, account):
        self.__name:str = name
        self.__address:str = address
        self.__email:str = email
        self.__phone:str = phone
        self.__account:str = account

class Customer(Person):
    def __init__(self, frequent_flyer_number):
        self.__frequent_flyer_number:int

    def get_itineraries(self):
        pass

class Passenger:
    def __init__(self, name, passport_number, date_of_birth):
        self.__name: List[int] = name
        self.__passport_number = passport_number
        self.__date_of_birth = date_of_birth


# Airport, Aircraft, Seat, and FlightSeat

class Airport:
    def __init__(self, name, address, code):
        self.__name = name
        self.__address = address
        self.__code = code
    
    def get_flights(self):
        None

class Seat:
    def __init__(self, seat_number, type, seat_class):
        self.__seat_number = seat_number
        self.__type = type
        self.__seat_class = seat_class

class FlightSeat(Seat):
    def __init__(self, fare):
        self.__fare = fare
    
    def get_fare(self):
        return self.__fare



# FlightSchedule, Flight, FlightInstance, FlightReservation, Itinerary

# class WeeklySchedule:
#     def __init__(self, day_of_week, departure_time):
#         self.




