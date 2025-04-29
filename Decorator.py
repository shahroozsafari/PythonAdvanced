
def prettyoutput(my_function) :
    def wrapper(*a):
        print(40*"*")
        my_function(*a)
        print(40*"*")
        return my_function
    return wrapper

@prettyoutput
def greetings(text):
    print(text)

@prettyoutput
def test(a,b):
    print(a+b)

greetings("Salam")
test(10,20)
