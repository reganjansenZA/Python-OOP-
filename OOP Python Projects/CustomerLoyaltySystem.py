class Customer:
    def __init__(self, customer_id, name):
        self.customer_id = customer_id
        self.name = name

class LoyaltyPoints:
    def __init__(self):
        self.points = 0

    def earn_points(self, amount):
        self.pointsd = amount

    def redeem_points(self, amount):
        if self.points >= amount:
            self.points -= amount
        else:
            print("Not enough Points")

    def show_point_balance(self):
        return self.points

class VIPcustomer(Customer, LoyaltyPoints):
    def __init__(self , customer_id, name):
        Customer.__init__(self, customer_id, name)
        LoyaltyPoints.__init__(self)

class Transactions:
    def __init__(self, transaction_id, customer, amount):
        self.transaction_id = transaction_id
        self.customer = customer
        self.amount = amount

class TransactionHistory:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def show_transaction(self):
        for transaction in self.transactions:
            print(transaction.transaction_id, transaction.customer ,transaction.amount)

vip = VIPcustomer("VIP003", "Regan Big Dick")
vip.earn_points(50000)
vip.redeem_points(125800)


transaction1 = Transactions("T-002", vip, "+5000")
transaction2 = Transactions("T-002", vip, "-1200")

transaction_history = TransactionHistory()
transaction_history.add_transaction(transaction1)
transaction_history.add_transaction(transaction2)

transaction_history.show_transaction()

balance = vip.show_point_balance()

print(f'Customer ID: {vip.customer_id}')
print(f'Customer Name: {vip.name}')
print(f'Loyalty Point Balance: {balance}')

