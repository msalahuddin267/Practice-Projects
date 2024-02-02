class Car:
    def __init__(self, name, model, year):
        self.name = name
        self.model = model
        self.year = year

    def display_parent(self):
        print("\nCar Information:")
        print(f"\t{self.year} {self.name} {self.model}")


class ElectricCar(Car):
    def __init__(self, name, model, year, battery_capacity):
        super().__init__(name, model, year)
        self.battery_capacity = battery_capacity

    def display_car_information(self):
        super().display_parent()
        print(f"\tBattery Capacity: {self.battery_capacity} kWh\n")


class GasCar(Car):
    def __init__(self, name, model, year, fuel_efficiency):
        super().__init__(name, model, year)
        self.fuel_efficiency = fuel_efficiency

    def display_car_information(self):
        super().display_parent()
        print(f"\tFuel Efficiency: {self.fuel_efficiency} MPG\n")


def main():
    while True:
        car_type = input("Enter car type (Electric/Gas): ").lower()
        
        if car_type not in ["electric", "gas"]:
            print("Invalid car type.")
            continue
        
        name = input("Enter Name: ")
        model = input("Enter model: ")
        year = input("Enter year: ")
        
        if car_type == "electric":
            battery_capacity = input("Enter battery capacity (kWh): ")
            car = ElectricCar(name, model, year, battery_capacity)
            
        else:
            fuel_efficiency = input("Enter fuel efficiency (MPG): ")
            car = GasCar(name, model, year, fuel_efficiency)
        
        car.display_car_information()

        if input("Are you enter another car? (yes/no): ").lower() == "no":
            break


# calling main
if __name__ == "__main__":
    main()
