from car import Car

def main():
    new_car = Car("BMW", "2018", 10000)
    new_car.printresults()  

    new_car.drive(100)  # Simulate driving
    new_car.printresults()  

if __name__ == "__main__":
    main()

