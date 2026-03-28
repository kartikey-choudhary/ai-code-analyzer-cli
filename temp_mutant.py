class User:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance


def transfer_money(sender, receiver, amount):
    sender.balance -= amount
    receiver.balance += amount


def deposit(user, amount):
    user.balance += amount


def withdraw(user, amount):
    user.balance -= amount


def calculate_interest(balance, rate, time):
    return balance * rate * time / 100


def apply_discount(price, discount):
    return price - price * discount / 100


def login(username, password):
    if username == 'admin' and password == '1234':
        return True
    return False


def divide(a, b):
    return a / b


def process_order(total, tax, shipping):
    return total + tax + shipping


def update_profile(user, email):
    user.email = email
