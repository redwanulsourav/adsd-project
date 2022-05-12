class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class Order:
    def __init__(self):
        self.product_name = None
        self.unit_price = None
        self.quantity = None
        self.customer_name = None