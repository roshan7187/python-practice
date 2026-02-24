class bank:
    min_balance = 500
    trans_limit = 100000
    ROI = 0.075

    def __init__(self,name,mobno,accno,balance):
        self.name = name
        self.mobno = mobno
        self.accno = accno
        self.balance = balance

    def deposit(self):
        if self.accno == int(input("Enter account number: ")):
            amount = int(input("Enter amount to deposit: "))
            if 500 <= amount <= 40000 and amount % 100 == 0:
                self.balance += amount
                return f"Deposited {amount}. New balance is {self.balance}."
            return "Invalid deposit amount."
        return "Invalid account number."
    def withdraw(self):
        if self.accno == int(input("Enter account number: ")):
            amount = int(input("Enter amount to withdraw: "))
            if amount <= self.balance and 500 <= amount <= 20000 and amount % 100 == 0:
                self.balance -= amount
                return f"Withdrew {amount}. New balance is {self.balance}."
            return "Invalid withdrawal amount."
        return "Invalid account number."


cust1 = bank("Alice", 1234567890, 785412654251, 10000)
cust2 = bank("Bob", 9876543212, 785412654252, 20000)
cust3 = bank("Charlie", 1122334455, 785412654253, 15000)

print(cust1.withdraw())