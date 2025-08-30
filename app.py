import sqlite3
from flask import Flask
from flask import abort, redirect, render_template, request, session
from werkzeug.security import check_password_hash, generate_password_hash
import config
import db

app = Flask(__name__)
app.secret_key = config.secret_key

def require_login():
    if "user_id" not in session:
        abort(403)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/new_fish")
def new_fish():
    require_login()
    return render_template("new_fish.html")

@app.route("/create_fish", methods=["POST"])
def create_fish():
    require_login()
    fish_name = request.form["fish_name"]
    weight = request.form["weight"]
    
    if not fish_name or not weight:
        abort(403)

    user_id = session["user_id"]
    db.add_fish(user_id, fish_name, weight)
    
    return redirect("/")


@app.route("/create", methods=["POST"])
def create():
    username = request.form["username"]
    if not username or len(username) > 20:
        return "VIRHE: tunnus ei voi olla tyhjä tai liian pitkä"
    password1 = request.form["password1"]
    if not password1:
        return "VIRHE: salasana ei voi olla tyhjä"
    password2 = request.form["password2"]
    if password1 != password2:
        return "VIRHE: salasanat eivät ole samat"
    password_hash = generate_password_hash(password1)

    try:
        sql = "INSERT INTO users (username, password_hash) VALUES (?, ?)"
        db.execute(sql, [username, password_hash])
    except sqlite3.IntegrityError:
        return "VIRHE: tunnus on jo varattu"

    return redirect("/login")



@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        sql = "SELECT id, password_hash FROM users WHERE username = ?"
        result = db.query(sql, [username])[0]
        user_id = result["id"]
        password_hash = result["password_hash"]

        if check_password_hash(password_hash, password):
            session["user_id"] = user_id
            session["username"] = username
            return redirect("/")
        return "VIRHE: väärä tunnus tai salasana"


@app.route("/logout")
def logout():
    if "user_id" in session:
        del session["user_id"]
        del session["username"]
    return redirect("/")