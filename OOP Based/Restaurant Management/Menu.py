class Food:
    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price
        self.cooking_time = 15

class Burger(Food):
    def __init__(self, name, price, meat, ingrediants) -> None:
        super().__init__(name, price)
        self.meat = meat
        self.ingrediants = ingrediants

class Pizza(Food):
    def __init__(self, name, price, size, ingrediants, toopings) -> None:
        super().__init__(name, price)
        self.size = size
        self.ingrediants = ingrediants
        self.toopings = toopings

class Drinks(Food):
    def __init__(self, name, price, is_cold = True) -> None:
        super().__init__(name, price)
        self.is_cold = is_cold

class Menu:
    def __init__(self) -> None:
        self.pizzas = []
        self.burgers = []
        self.drinks = []

    def add_menu_item(self, item_type, item):
        if item_type == 'pizza':
            self.pizzas.append(item)
        elif item_type == 'burger':
            self.burgers.append(item)
        elif item_type == 'drinks':
            self.drinks.append(item)

    def remove_pizza(self, pizza):
        if pizza in self.pizzas:
            self.pizzas.remove(pizza)

    def show_menu(self):
        for pizza in self.pizzas:
            print(f'name: {pizza.name}, price: {pizza.price}')
        for burger in self.burgers:
            print(f'name: {burger.name}, price: {burger.price}')
        for drink in self.drinks:
            print(f'name: {drink.name}, price: {drink.price}')