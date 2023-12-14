from app import app
import users
import comments
from flask import render_template, request, redirect
from db import db
import orders

@app.route("/")
def index():
    return render_template("frontpage.html")

@app.route("/profile")
def profile():
    return render_template("profile.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("profile.html")
    
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.login(username, password):
            return redirect("/profile")
        
        return render_template("error.html", message="Väärä tunnus tai salasana")
        
@app.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "GET":
        return render_template("create.html")
    
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if len(username) == 0:
            return render_template("error.html", message="Syötä käyttäjätunnus")
        if len(password) == 0:
            return render_template("error.html", message="Syötä salasana")
        if users.create(username, password):
            return redirect("/profile")
        else:
            return render_template("error.html", message="Rekisteröinti ei onnistunut")

@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")

@app.route("/comments")
def comments_route():
    commentslist = comments.get_list()
    rating = comments.get_average_rating()
    return render_template("comments.html", commentslist=commentslist, rating=rating)

@app.route("/send", methods=["GET", "POST"])
def send():
    if request.method == "GET":
        return render_template("profile.html")

    if request.method == "POST":
        users.check_csrf()

        comment = request.form["comment"]
        if len(comment) > 100:
            return render_template("/error.html", message="Kommentti on liian pitkä")
        if len(comment) == 0:
            return render_template("/error.html", message="Kommentti on tyhjä")
        
        if comments.add_comment(comment):
            return render_template("profile.html")
        
@app.route("/rate", methods=["GET", "POST"])
def rate():
    if request.method == "GET":
        return render_template("profile.html")
    if request.method == "POST":
        users.check_csrf()
        rating = request.form["rating"]
        if comments.add_rating(rating):
            return render_template("profile.html")
        
        return render_template("/error.html", message="Arvostelu ei onnistunut")

@app.route("/order")
def order():
    most_ordered_pizza = orders.get_most_ordered_pizza()
    most_ordered_drink = orders.get_most_ordered_drink()
    return render_template("order.html", most_pizzas=most_ordered_pizza, most_drinks=most_ordered_drink)

@app.route("/result", methods=["POST"])
def result():
    pizzas = request.form.getlist("pizza")
    drinks = request.form.getlist("drink")
    message = request.form["message"]
    address = request.form["address"]

    if len(address) == 0:
        return render_template("error.html", message="Anna osoite ja saapumisohjeet")

    if orders.add_order(pizzas) and orders.add_drink_order(drinks):
        return render_template("result.html", pizzas=pizzas, message=message, drinks=drinks, address=address)
    else:
        return render_template("error.html", message="Tilaus ei onnistunut")
    
@app.route("/personal_stats")
def personal_stats():
    username = users.username()
    spent = orders.user_total_spending(username)
    list = orders.all_user_orders(username)
    favorite_pizza = orders.get_favorite_pizza(username)
    favorite_drink = orders.get_favorite_drink(username)
    return render_template("personal_stats.html", spent=spent, list=list, favorite_pizza=favorite_pizza, favorite_drink=favorite_drink)
