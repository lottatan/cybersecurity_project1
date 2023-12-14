from werkzeug.security import check_password_hash, generate_password_hash
from flask import session, request, abort
from db import db
from sqlalchemy.sql import text
import os


def create(username, password):
    hash_value = generate_password_hash(password)
    try:
        sql = text("INSERT INTO users (username, password) VALUES (:username, :password)")
        db.session.execute(sql, {"username":username, "password":hash_value})
        db.session.commit()
    except:
        return False
    
    return login(username, password)

    
def login(username, password):
    sql = text("SELECT id, password FROM users WHERE username=:username")
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()
    if not user:
        return False
    else:
        session["user_id"] = user[0]
        if check_password_hash(user.password, password):
            session["username"] = username
            session["csrf_token"] = os.urandom(16).hex()
            return True

def logout():
    try:
        del session["user_id"]
        del session["username"]
    except:
        return

def user_id():
    return session.get("user_id", 0)

def username():
    return session.get("username")

def check_csrf():
    if session["csrf_token"] != request.form["csrf_token"]:
        abort(403)