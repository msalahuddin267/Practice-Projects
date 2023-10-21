from Users import Chef, Customer, Food_Server, Manager
from Restaurant import Restaurant
from Menu import Pizza, Burger, Drinks, Menu
from Order import Order

def main():
    menu = Menu()
    pizza_1 = Pizza('beef chess', 800, 'medium', ['beef', 'chees', 'saus'], 'top1')
    menu.add_menu_item('pizza', pizza_1)
    pizza_2 = Pizza('chicken chess', 800, 'large', ['chicken', 'chees', 'saus'], 'top2')
    menu.add_menu_item('pizza', pizza_2)

    burger_1 = Burger('naga beef', 500, 'beef', ['beef', 'spicy', 'bread'])
    menu.add_menu_item('burger', burger_1)
    burger_2 = Burger('naga chicken', 400, 'chicken', ['chicken', 'spicy', 'bread'])
    menu.add_menu_item('burger', burger_2)

    drink_1 = Drinks('coke', 150, True)
    menu.add_menu_item('drinks', drink_1)
    drink_2 = Drinks('fanta', 120, True)
    menu.add_menu_item('drinks', drink_2)

    menu.show_menu()

    restaurant = Restaurant('Dhaka Restaurant', 1000, menu)

    manager = Manager('manage babu', 17, 'mb@cupa.com', 'babu nagar', 2000, '1 March, 2022', 'core')
    restaurant.add_employee('manager', manager)

    chef = Chef('Altab baburchi', 19, 'ab@cupa.com', 'cupa nagar', 1500, '1 may, 2023', 'chec', 'everythings')
    restaurant.add_employee('chef', chef)

    food_server = Food_Server('mr been', 18, 'ben@cupa.com', 'cupa nagar', 1000, '1 june, 2022', 'food_server')
    restaurant.add_employee('food_server', food_server)

    restaurant.show_employees()

    # customer_1 placing order
    customer_1 = Customer('sakib', 17, 'sakib@cupa.com', 'gulsan', 10000)
    order_1 = Order(customer_1, [pizza_1, burger_1, drink_2])
    customer_1.pay_for_order(order_1)
    restaurant.add_order(order_1)
    
    # customer_1 paying for oder_1
    restaurant.receive_payment(order_1, 2000, customer_1)

    # customer_2 placing order
    customer_2 = Customer('rakib', 17, 'rakib@cupa.com', 'banani', 20000)
    order_2 = Order(customer_2, [pizza_2, drink_1, burger_1, burger_2])
    customer_1.pay_for_order(order_2)
    restaurant.add_order(order_2)
    
    # customer_2 paying for oder_2
    restaurant.receive_payment(order_2, 5000, customer_2)
    
    print(f'revenue: {restaurant.revenue} balance: {restaurant.balance}')

    # Restaurant expense 
    restaurant.pay_expense(restaurant.rent, 'rent')
    restaurant.pay_salary(chef)

    print(f'After expense - revenue: {restaurant.revenue} balance: {restaurant.balance} expense: {restaurant.expense}')


# calling main
if __name__ == '__main__':
    main()