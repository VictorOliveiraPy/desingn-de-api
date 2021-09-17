from coopy.base import init_persistent_system


class Order:
    def __init__(self, coffe, size, milk, location, id=None):
        self.id = id
        self.coffe = coffe
        self.size = size
        self.milk = milk
        self.location = location


class CoffeShop:
    def __init__(self):
        self.orders = {}

    def place_order(self, order):
        if order.id is None:
            order.id = len(self.orders) + 1

        self.orders[order.id] = order
        return order

