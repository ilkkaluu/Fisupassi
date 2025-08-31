import secrets, sqlite3
from flask import Flask
from flask import abort, redirect, render_template, request, session
from werkzeug.security import check_password_hash, generate_password_hash
import config
import fish
import db

app = Flask(__name__)
app.secret_key = config.secret_key

def require_login():
    if "user_id" not in session:
        abort(403)

def check_csrf_token():
    if request.form["csrf_token"] != session.get("csrf_token"):
        abort(403)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/user")
def user_profile():
    require_login()
    username = session["username"]
    fish_list = fish.get_user_fish(session["user_id"])
    search_result = None
    fish_search = request.args.get("fish_search")
    if fish_search:
        filtered = [f for f in fish_list if f["fish_name"] == fish_search]
        search_result = len(filtered)
    return render_template('user.html', username=username, fish_list=fish_list, search_result=search_result, fish_search=fish_search)

@app.route("/new_fish")
def new_fish():
    require_login()
    return render_template("new_fish.html")

@app.route("/create_fish", methods=["POST"])
def create_fish():
    require_login()
    check_csrf_token()
    fish_name = request.form["fish_name"]
    weight = request.form["weight"]
    
    if not fish_name or not weight:
        abort(403)

    user_id = session["user_id"]
    fish.add_fish(user_id, fish_name, weight)
    
    return redirect("/")

@app.route("/edit_fish/<int:id>", methods=["POST"])
def edit_fish(id):
    require_login()
    check_csrf_token()
    fish_to_edit = fish.get_fish(id)
    if not fish_to_edit:
        abort(404)
    if fish_to_edit["user_id"] != session["user_id"]:
        abort(403)
    return render_template("edit_fish.html", fish=fish_to_edit)

@app.route("/update_fish", methods=["POST"])
def update_fish():
    require_login()
    check_csrf_token()
    fish_id = request.form["id"]
    fish_to_update = fish.get_fish(fish_id)
    if not fish_to_update:
        abort(404)
    if fish_to_update["user_id"] != session["user_id"]:
        abort(403)
    fish_name = fish_to_update["fish_name"]
    if request.form.get("fish_name") is not None:
        fish_name = request.form["fish_name"]
    if not fish_name:
        abort(403)
    weight = request.form["weight"]
    if not weight:
        abort(403)

    fish.edit_fish(fish_id, fish_name, weight)
    return redirect("/user")

@app.route("/remove_fish/<int:id>", methods=["POST"])
def remove_fish(id):
    require_login()
    check_csrf_token()
    fish.remove_fish(id)
    return redirect("/user")

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
            session["csrf_token"] = secrets.token_hex(16)
            session["username"] = username
            return redirect("/")
        return "VIRHE: väärä tunnus tai salasana"


@app.route("/logout")
def logout():
    if "user_id" in session:
        del session["user_id"]
        del session["username"]
    return redirect("/")