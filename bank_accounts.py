class BankAccount:
    def __init__(self, first_name, last_name, account_id, account_type, pin, balance):
        self.first_name = first_name
        self.last_name = last_name
        self.account_id = account_id
        self.account_type = account_type
        self.pin = pin
        self.balance = balance

    def deposit(self):
        self.balance += float(input("Enter deposit amount"))
        return(self.balance)
    
    def withdraw(self):
        self.balance -= float(input("Enter amount to withdraw"))
        return(self.balance)
    
    def display_balance(self):
        print(self.balance)
chase = BankAccount("AJ", "Flory", 696969, "Savings", 69420, 30.02)

chase.deposit()
chase.withdraw()
chase.display_balance()