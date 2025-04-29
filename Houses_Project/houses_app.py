
class House :

    def __init__(self, area, builtin_year, price, parking):
        self.area =area
        self.builtin_year = builtin_year
        self.price = price
        self.parking = parking

    def mortgage_calc(self) :
        pass

    def promotion(self) :
        pass

class Owner :
    pass

class RentalHouse(House) :
    pass
