
class SmartPhone :
    os = "Android"
    def __init__(self, brand, model, size, camera, weight, cpu):
        self.brand = brand
        self.model = model 
        self.size = size
        self.camera = camera 
        self.weught = weight
        self.cpu = cpu 
        self.price = 0


#----------------- Main -----------------------
phone1 = SmartPhone("Samsung","S25",6.9,200,218,"snapdragon")
