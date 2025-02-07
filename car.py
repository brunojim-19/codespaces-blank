class Car:
    def __init__(self, model, year, mileage):
        self.model = model
        self.year = year
        self.mileage = mileage
        


    def drive(self, miles):
        self.mileage += miles
        print(f"The car has been driven {miles} miles. Total mileage is now {self.mileage} miles.")


    def printresults(self):
       print(f"Car Information: \nModel: {self.model}\nYear: {self.year}\nMileage: {self.mileage}")




      