
import flask
from cars_app import Car, UserPass, PrimaryKeyError, YearError, PriceError, UsernameError

def hash_password(password):
    import hashlib
    hash_algo = hashlib.new("SHA256")
    hash_algo.update(password.encode())
    hashed_password = hash_algo.hexdigest()
    return hashed_password

webapp =flask.Flask(__name__,)

@webapp.route('/')
def index():
    return flask.render_template("index.html")

@webapp.route("/about")
def about():
    return flask.render_template("about.html")

@webapp.route("/carslist")
def carslist():
    return flask.render_template("carslist.html",allcars=Car.carslist())


@webapp.route("/newcar",methods=["POST","GET"])
def newcar():
    if flask.request.method == "POST" :
        car = dict(flask.request.form)
        try:
            Car(car["carid"],car["maker"],car["model"],int(car["year"]),float(car["price"]),car["color"])
        except(PrimaryKeyError) :
            return flask.render_template("error.html",error_text="This Car ID already exists in database ")
        except(YearError) :
            return flask.render_template("error.html",error_text = "Year must be after 2020 !")
        except(PriceError):
            return flask.render_template("error.html",error_text = "Price must be between 20K and 150K !")
        return flask.redirect("/")
    return flask.render_template("newcar.html")

@webapp.route("/deletecar",methods=["POST","GET"])
def deletecar():
    if flask.request.method == "POST" :
        carid = dict(flask.request.form)
        Car.delete_car(int(carid["carid"]))
        return flask.redirect("/carslist")
    return flask.render_template("deletecar.html")

@webapp.route("/signup",methods=["POST","GET"])
def signup():
    if flask.request.method == "POST" :
        userpass = dict(flask.request.form)
        hash_pwd = hash_password(userpass["password"])
        try:
            UserPass(userpass["username"],hash_pwd)
        except(UsernameError):
            return flask.render_template("error.html",error_text="This Username has been taken !")
        return flask.redirect("/")
    return flask.render_template("signup.html")

@webapp.route("/login",methods=["POST","GET"])
def login():
    if flask.request.method == "POST" :
        userpass = dict(flask.request.form)
        hash_pwd = hash_password(userpass["password"])
        check = UserPass.check(userpass["username"],hash_pwd)
        if check :
            return flask.redirect("/carslist")
        else:
            return flask.render_template("error.html",error_text="Invalid Username or Password !")

    return flask.render_template("login.html")

webapp.run(debug=True)