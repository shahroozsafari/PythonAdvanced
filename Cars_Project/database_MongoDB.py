
import pymongo

connection = pymongo.MongoClient("mongodb://localhost:27017")

database = connection["cars_database"]
collection = database["cars_collection"]
owenr_collection = database["Owner_Collection"]

owenr_collection.insert_one({"first name":"Ali","last name":"Ahmadi","code melli":"0036526598"})


def insert_car(car_id,maker,model,year,price,color) :
    collection.insert_one({"car_id":car_id,"maker":maker,"model":model,"year":year,
                           "price":price,
                            "color":color})

def findcar(carid):
    car = list(collection.find({"car_id":carid},{"_id":0, "car_id":1,"maker":1, "model":1, "year":1,"price":1}))
    print(car)

def delete_car(carid) :
    collection.delete_many({"car_id":carid})

def update_year() :
    collection.update_many({"year":2023},{"$set":{"year":2026}})