class Order:
    def __init__(self, custormer, items) -> None:
        self.customer = custormer
        total = 0
        for item in items:
            total += item.price
        self.bill = total
        self.items = items