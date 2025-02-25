import random

class UserData:
    def __init__(self, name, account_number, amount, date_of_birth):
        self.name = name
        self.account_number = account_number
        self.amount = amount
        self.date_of_birth = date_of_birth

    def withdraw(self, amount):
        if self.amount >= amount:
            self.amount -= amount
            return f"Withdrawal of ₹{amount} successful. Remaining balance: ₹{self.amount}\n"
        return "Insufficient funds!\n"

    def deposit(self, amount):
        self.amount += amount
        return f"Deposit of ₹{amount} successful. Current balance: ₹{self.amount}\n"

def generate_random_account_number():
    return ''.join(str(random.randint(0, 9)) for _ in range(10))

def add_user(users, name, amount, dob):
    account_number = generate_random_account_number()
    users[name] = UserData(name, account_number, amount, dob)
    return "User added successfully!\n"

def check_amount(users, name, dob):
    user = users.get(name)
    if user and user.date_of_birth == dob:
        return f"Amount Of {name} with date of birth {dob}: ₹{user.amount}\n"
    return "User not found or date of birth doesn't match!\n"
