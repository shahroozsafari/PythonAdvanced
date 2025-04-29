
import database_SQLite as database

class YearError(Exception) :
    pass
class PriceError(Exception):
    pass
class PrimaryKeyError(Exception):
    pass
class UsernameError(Exception):
    pass

class Car :
    '''
    This is Car class.
    '''
    wheels = 4
    count = 0
    def __init__(self,car_id, maker, model, year, price, color="White"):
        self.car_id = car_id
        self.maker = maker
        self.model = model
        self.year = year
        self.price = price
        self.color = color
        self.checkup = []
        self.__maxprice = 150000        # Private
        self._test = 100                # Protected (Convension)
        Car.count+=1
        try:
            database.insert_car(self.car_id,self.maker,self.model,self.year,self.price,self.color)
        except(database.sqlite3.IntegrityError) :
            raise PrimaryKeyError

    def last_checkup(self,date) :
        self.checkup.append(date)
    
    def leased(self, months) :
        return self.price*1.1 / months
    
    def setmaxprice(self,p) :
        self.__maxprice = p 

    @property
    def price(self) :
        return self.p
    @price.setter
    def price(self, value) :
        if 20000 <= value <= 150000 :
            self.p = value
        else:
            raise PriceError("Price must be between 20K and 150K !")
    
    @property
    def year(self) :
        return self.y
    @year.setter
    def year(self, value) :
        if value >= 2020 :
            self.y = value
        else :
            raise YearError("Year must be greater than 2020")

    @staticmethod
    def discount(date) :
        print(f"All car are sold within 10% discount until {date}")

    @staticmethod
    def find_car(carid) :
        return database.findcar(carid)
    
    @staticmethod
    def updat_price(carid,price) :
        database.update_price(carid,price)
    
    @staticmethod
    def delete_car(carid) :
        database.delete_car(carid)

    @staticmethod
    def carslist():
        return database.carslist()

    @classmethod
    def cars_count(cls) :
        print("Number of sold cars = ",cls.count)
    
    def __str__(self):
       print( self.maker, self.model, self.price)
       return ""
    
    def __repr__(self):
        return "This is Car class"
    
    def __len__(self) :
        return len(self.checkup)
    
    def __getitem__(self, i) :
        return self.checkup[i]
    
    def __setitem__(self, i , v) :
        self.checkup.insert(i,v)
    
    def __call__(self, year,price,type):
        self.price = price
        self.year = year
        self.type = type

    def __add__(first,second) :
        add = first.price + second.price
        return add
    
    def __sub__(first,second) :
        pass

    def __del__(self) :
        print("--------------------------")

class Owner :
    def __init__(self, first_name, last_name, code_melli, birthdate, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.code_melli = code_melli
        self.birthdate = birthdate
        self.phone = phone
        self.visit_date = []
        

    def visit_date(self):
        print(self.visit_date)  

    # Setter - Getter for code melli


class Truck(Car) :
    def __init__(self, maker, model, year, price, load, passenger, color="White"):
        super().__init__(maker, model, year, price, color)
        self.load = load
        self.passenger = passenger
    
    def leased(self, months) :
        return self.price*1.15 / months
    
class HeavyDuty(Truck):
    def __init__(self, maker, model, year, price, load, passenger,axel, color="White"):
        super().__init__(maker, model, year, price, load, passenger, color)
        self.axel = axel

class UserPass :
    def __init__(self,username, password):
        self.username = username
        self.password = password
        try:
            database.insert_user(self.username,self.password)
        except(database.sqlite3.IntegrityError) :
            raise UsernameError 
    @staticmethod
    def check(username, password):
        return database.check_userpass(username, password)

# --------------- Main ---------------------

# car1= Car(10100,"Mazda","CX5",2024,50000,"Silver")
# car2= Car(10101,"Benz","S500",2023,97000)
# car3= Car(10107,"BMW","528i",2023,80000)
# trk1 = Truck(10103,"Ford","F150",2025,67000,2500,5,"Red")
# hed1 = HeavyDuty("Ford","450",2023,120000,6000,2,3,"Black")
# owner = Owner("Ali","Ahmadi","0036526598","1360/06/08","09126532659")

# car1.last_checkup("2024/10/15")
# car1.last_checkup("2024/12/15")

# print(car1)                     # __str__
# print(repr(car1))               # __repr__
# print(len(car1))                # __len__
# print(car1[1])                  # __getitem__
# car1[2] = "2025/03/01"          # __setitem__
# car1(2023,51000,"SUV")          # __call__
# print(car1+car2)                # __add__
# print(car1.__doc__)             # __doc__
# print(car1.__dict__)            # __dict__
# car1.leased(36)                 # Polymorphism
# trk1.leased(36)                 # Polymorphism
# Car.discount("2024/06/05")      # staticmethod
# Car.cars_count()                # classmethod

# car = car1.__dict__
# car["price"]=car.pop("p")
# car["year"] = car.pop("y")
# database.collection.insert_one(car)       # Insert to MongoDB