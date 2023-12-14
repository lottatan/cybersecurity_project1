from flask import session, request, abort
from db import db
from sqlalchemy.sql import text
import users
import datetime

def add_order(list):
    user_id = users.user_id()
    if user_id == "0":
        username = "anonymous"
    else:
        username = users.username()

    sum = 0
    i = 1


    for item in list:
        sum += int(item)*15
        if int(item) > 0:
            for j in range(int(item)):
                if i == 1:
                    pizza = "Marinara"
                elif i == 2:
                    pizza = "Margherita"
                elif i == 3:
                    pizza = "Pepperoni"
                elif i == 4:
                    pizza = "Salami"
                elif i == 5:
                    pizza = "Hawaii"
                elif i == 6:
                    pizza = "Quattro Formaggi"
                sql = text("INSERT INTO pizza_orders (username, pizza) VALUES (:username, :pizza)")
                db.session.execute(sql, {"username":username, "pizza":pizza})
                db.session.commit()
        i += 1


    sql = text("INSERT INTO orders (username, amount, ordered) VALUES (:username, :amount, NOW())")
    db.session.execute(sql, {"username":username, "amount":sum, "ordered":datetime.datetime.now()})
    db.session.commit()
    return True


def add_drink_order(list):
    user_id = users.user_id()
    if user_id == "0":
        username = "anonymous"
    else:
        username = users.username()
    
    sum = 0
    i = 1

    for item in list:
        sum += int(item)*3
        if int(item) > 0:
            for j in range(int(item)):
                if i == 1:
                    drink = "Coca-Cola"
                elif i == 2:
                    drink = "Coca-Cola Zero"
                elif i == 3:
                    drink = "Pepsi"
                elif i == 4:
                    drink = "Pepsi Max"
                elif i == 5:
                    drink = "Fanta"
                elif i == 6:
                    drink = "Sprite"
                sql = text("INSERT INTO drink_orders (username, drink) VALUES (:username, :drink)")
                db.session.execute(sql, {"username":username, "drink":drink})
                db.session.commit()
        i += 1

    sql = text("INSERT INTO orders (username, amount, ordered) VALUES (:username, :amount, NOW())")
    db.session.execute(sql, {"username":username, "amount":sum, "ordered":datetime.datetime.now()})
    db.session.commit()
    return True


def user_total_spending(username):
    sql = text("SELECT SUM(amount) FROM orders WHERE username=:username")
    result = db.session.execute(sql, {"username": username})
    return_value = result.fetchone()
    if return_value == None:
        return "Nolla"
    return return_value[0]


def all_user_orders(username):
    sql = text("SELECT amount, ordered FROM orders WHERE username=:username")
    result = db.session.execute(sql, {"username": username})
    return result.fetchall()

def get_favorite_pizza(username):
    sql = text("SELECT pizza FROM pizza_orders WHERE username=:username GROUP BY pizza ORDER BY COUNT(pizza) DESC LIMIT 1")
    result = db.session.execute(sql, {"username": username})
    return_value = result.fetchone()
    if return_value == None:
        return "No ordered pizzas"
    return return_value[0]

def get_favorite_drink(username):
    sql = text("SELECT drink FROM drink_orders WHERE username=:username GROUP BY drink ORDER BY COUNT(drink) DESC LIMIT 1")
    result = db.session.execute(sql, {"username": username})
    return_value = result.fetchone()
    if return_value == None:
        return "No ordered drinks"
    return return_value[0]

def get_most_ordered_pizza():
    sql = text("SELECT pizza FROM pizza_orders GROUP BY pizza ORDER BY COUNT(pizza) DESC LIMIT 1")
    result = db.session.execute(sql)
    return_value = result.fetchone()
    if return_value == None:
        return "No ordered pizzas"
    return return_value[0]


def get_most_ordered_drink():
    sql = text("SELECT drink FROM drink_orders GROUP BY drink ORDER BY COUNT(drink) DESC LIMIT 1")
    result = db.session.execute(sql)
    return_value = result.fetchone()
    if return_value == None:
        return "No ordered drinks"
    return return_value[0]

def get_deliverytime_and_amount():
    sql1 = text("SELECT delivery_time FROM orders ORDER BY DESC LIMIT 1")
    delivery = db.session.execute(sql1)
    delivery2 = delivery.fetchone()[0]
    sql2 = text("SELECT amount FROM orders ORDER BY DESC LIMIT 1")
    delivery = db.session.execute(sql2)
    delivery3 = delivery.fetchone()[0]

    return delivery2