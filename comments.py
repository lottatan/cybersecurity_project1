from sqlalchemy.sql import text
from flask import session
from db import db
import datetime
import users


def get_list():
    sql = text("SELECT username, comment, posted FROM comments")
    result = db.session.execute(sql)
    return result.fetchall()

def add_comment(comment):
    username = users.username()
    sql = text("INSERT INTO comments (username, comment, posted) VALUES (:username, :comment, NOW())")
    db.session.execute(sql, {"username":username, "comment":comment, "posted":datetime.datetime.now()})
    db.session.commit()
    return True

def add_rating(rating):
    username = users.username()
    sql = text("INSERT INTO ratings (username, rating, posted) VALUES (:username, :rating, NOW())")
    db.session.execute(sql, {"username":username, "rating":rating, "posted":datetime.datetime.now()})
    db.session.commit()
    return True

def get_average_rating():
    sql = text("SELECT ROUND(AVG(rating),0) as avg_rating FROM ratings")
    result = db.session.execute(sql)
    return result.fetchone()[0]