
class Person :
    university = "IUT"
    def __init__(self,first_name, last_name, code_melli, birthdate):
        self.first_name = first_name
        self.last_name = last_name
        self.code_melli = code_melli
        self.birthdate = birthdate

    def salary_calculate(self, hour) :
        if hour <= 40 :
            return hour*100000
        else :
            return 40*100000 + (hour-40)*140000
        
    def __del__(self):
        print("*************")

class Teacher(Person):
    def __init__(self, first_name, last_name, code_melli, birthdate, courses=[]):
        super().__init__(first_name, last_name, code_melli, birthdate)
        self.courses = courses

    def schdule():
        pass
        

class Student(Person) :
    pass

class staff(Person) :
    pass

#------------------------
teacher1 = Teacher("Shahrooz","Safari",1234567890,"5424",["C++","Python"])

print(teacher1.first_name)