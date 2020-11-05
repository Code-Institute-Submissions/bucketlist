import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/get_intentions")
def get_intentions():
    intentions = list(mongo.db.intentions.find())
    return render_template("intentions.html", intentions=intentions)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                        session["user"] = request.form.get("username").lower()
                        flash("Welcome, {}".format(
                            request.form.get("username")))
                        return redirect(url_for(
                            "profile", username=session["user"]))
            else:
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_intention", methods=["GET", "POST"])
def add_intention():
    if request.method == "POST":
        intention = {
            "division_name": request.form.get("division_name"),
            "intention_name": request.form.get("intention_name"),
            "intention_description": request.form.get("intention_description"),
            "due_date": request.form.get("due_date"),
            "created_by": session["user"]
        }
        mongo.db.intentions.insert_one(intention)
        flash("Intention Successfully Added")
        return redirect(url_for("get_intentions"))

    divisions = mongo.db.divisions.find().sort("division_name", 1)
    return render_template("add_intention.html", divisions=divisions)


@app.route("/edit_intention/<intention_id>", methods=["GET", "POST"])
def edit_intention(intention_id):
    if request.method == "POST":
        submit = {
            "division_name": request.form.get("division_name"),
            "intention_name": request.form.get("intention_name"),
            "intention_description": request.form.get("intention_description"),
            "due_date": request.form.get("due_date"),
            "created_by": session["user"]
        }
        mongo.db.intentions.update({"_id": ObjectId(intention_id)}, submit)
        flash("Intention Successfully Updated")

    intention = mongo.db.intentions.find_one({"_id": ObjectId(intention_id)})
    divisions = mongo.db.divisions.find().sort("division_name", 1)
    return render_template("edit_intention.html", intention=intention, divisions=divisions)


@app.route("/delete_intention/<intention_id>")
def delete_intention(intention_id):
    mongo.db.intentions.remove({"_id": ObjectId(intention_id)})
    flash("Intention Successfully Deleted")
    return redirect(url_for("get_intentions"))


@app.route("/get_divisions")
def get_divisions():
    divisions = list(mongo.db.divisions.find().sort("division_name", 1))
    return render_template("divisions.html", divisions=divisions)


@app.route("/add_division", methods=["GET", "POST"])
def add_division():
    if request.method == "POST":
        division = {
            "division_name": request.form.get("division_name")
        }
        mongo.db.divisions.insert_one(division)
        flash("New Division Added")
        return redirect(url_for("get_divisions"))

    return render_template("add_division.html")


@app.route("/edit_division/<division_id>", methods=["GET", "POST"])
def edit_division(division_id):
    if request.method == "POST":
        submit = {
            "division_name": request.form.get("division_name")
        }
        mongo.db.divisions.update({"_id": ObjectId(division_id)}, submit)
        flash("Division Successfully Updated")
        return redirect(url_for("get_divisions"))

    division = mongo.db.divisions.find_one({"_id": ObjectId(division_id)})
    return render_template("edit_division.html", division=division)


@app.route("/delete_division/<division_id>")
def delete_division(division_id):
    mongo.db.divisions.remove({"_id": ObjectId(division_id)})
    flash("Division Successfully Deleted")
    return redirect(url_for("get_divisions"))


@app.route("/delete-profile/<user_id>", methods=["GET", "POST"])
def delete_profile(user_id):
    mongo.db.users.remove({"username": session["user"]})
    session.clear()
    flash("Your profile has been deleted.")
    return redirect(url_for("get_intentions"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)