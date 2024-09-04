#Name: Cameron Gilmour
# Program: vehicle info app
# file: M03Lab.py
#description: app to put together user inputed information about vehicles

class Vehicle:
    def __init__(self,vehicle_type):
        self.vehicle_type = vehicle_type

class Automobile(Vehicle):
    def __init__(self, year, make, model, doors, roof):
        super().__init__("car")
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof


def main():
    print("Welcome to the car info app")
    year = input("Enter the model year of the car: ")
    make = input("Enter the make of the vehicle: ")
    model = input("Enter the model of the vehicle: ")
    doors = input("Enter the number of doors 2 or 4: ")
    roof = input("Enter type of roof (solid or sun roof): ")
    
    car = Automobile(year,make,model,doors,roof)

    print("\nCar Information:")
    print(f"  Vehicle type: {car.vehicle_type}")
    print(f"  Year: {car.year}")
    print(f"  Make: {car.make}")
    print(f"  Model: {car.model}")
    print(f"  Number of doors: {car.doors}")
    print(f"  Type of roof: {car.roof}")




if __name__== "__main__":
    main()
        