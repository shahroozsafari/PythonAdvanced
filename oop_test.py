
class Student :
    University = "Tehran Uni"
    def __init__(self,fname,lname,stdcode,age):
        self.first_name = fname
        self.last_name = lname
        self.std_code = stdcode
        self.age = age
        self.grades = []

    def average(self) :
        if len(self.grades) == 0 :
            return 0
        return round(sum(self.grades) / len(self.grades) ,2)
    
    @property
    def first_name(self) :
        return self.fn
    @first_name.setter
    def first_name(self, value) :
        value = value.replace(" ","")
        if value.isalpha() :
            self.fn = value
        else : 
            raise ValueError("Invalid Name !")


    def __del__(self) :
        print("Goodbye ...")



std1 = Student("Amin mohamad","Ahmadi",10100,21)


# print(Student.__sizeof__())
# std1.grades.append(16)
# std1.grades.append(19)
# std1.grades.append(15)

# print(std1.average())
