class Car:
     def __init__(self, car_brand, car_model, car_price, car_color, manifacture_year):
          self.car_brand = car_brand
          self.car_model = car_model
          self.car_price = car_price
          self.car_color = car_color
          self.manifacture_year = manifacture_year
     def display_info(self):
        print(self.car_brand, self.car_model, self.car_price, self.car_color, self.manifacture_year)

def sort_price():
    cars.sort(key = lambda car: car.car_price, reverse=True)
    for i in range(len(cars)):
        print(cars[i].display_info())

def list_by_brand(brand):
    for i in range(len(cars)):
       if(cars[i].car_brand == brand):
           print(cars[i].display_info())

def search_color(color):
    carToPrint = Car("", "", 0, "", 0)
    
    for i in range(len(cars)):
        if cars[i].car_color == color:
            if cars[i].car_price > carToPrint.car_price:
                carToPrint = cars[i]
    
    print(carToPrint.display_info())


cars = []
car1 = Car("Mercedes", "G class", 140000, "black", 2018)
car2 = Car("Audi", "A7", 200000, "black", 2022)
car3 = Car("BMW", "M5", 100000, "white", 2020)
car4 = Car("Mercedes", "S class", 120000, "black", 2019)
car5 = Car("Audi", "Q8", 150000, "red", 2021)
car6 = Car("BMW", "X6", 170000, "red", 2021)
car7 = Car("Porsche", "Cayenne", 200000, "white", 2023)

cars.append(car1)
cars.append(car2)
cars.append(car3)
cars.append(car4)
cars.append(car5)
cars.append(car6)
cars.append(car7)


sort_price()
brandInp = input("Type brand: ")
list_by_brand(brandInp)
colorInp = input("Type color: ")
search_color(colorInp)


