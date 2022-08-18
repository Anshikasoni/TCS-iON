from flask import Flask, url_for, render_template, request, redirect, session
from werkzeug.security import check_password_hash, generate_password_hash
import os.path
import sqlite3

conn = sqlite3.connect(os.path.abspath("ion.project"), check_same_thread=False)
c = conn.cursor()

app = Flask(__name__)
app.config["SECRET_KEY"] = "secretkey"

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if the form is valid

            if not request.form.get("email") or not request.form.get("password") or not request.form.get("confirmation"):
                return "please fill out all fields"

            if request.form.get("password") != request.form.get("confirmation"):
                return "password confirmation doesn't match password"

            # check if email exist in the database
            exist = c.execute("SELECT * FROM users WHERE email=:email", {"email": request.form.get("email")}).fetchall()

            if len(exist) != 0:
                return "user already registered"

            # hash the password
            pwhash = generate_password_hash(request.form.get("password"), method="pbkdf2:sha256", salt_length=8)

            # insert the row
            c.execute("INSERT INTO users (email, password) VALUES (:email, :password)", {"email": request.form.get("email"), "password": pwhash})
            conn.commit()

            # return success
            return "registered successfully!"
    else:
        return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":
        # check the form is valid
        if not request.form.get("email") or not request.form.get("password"):
            return "please fill out all required fields"

        # check if email exist in the database
        user = c.execute("SELECT * FROM users WHERE email=:email", {"email": request.form.get("email")}).fetchall()

        if len(user) != 1:
            return "you didn't register"

        # check the password is same to password hash
        print(user)
        pwhash = user[0][1]
        if check_password_hash(pwhash, request.form.get("password")) == False:
            return "wrong password"

        # login the user using session
        session["user_id"] = user[0][0]
        session["user_type"] = user[0][2]
        # return success
        return redirect("/home")

    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

@app.route("/home")
def home():
    contacts = c.execute("SELECT * FROM contactus").fetchall()
    print(contacts)
    return render_template("home.html", contacts=contacts)

@app.route("/contactUs", methods=["GET", "POST"])
def contactUs():
    if request.method == "POST":
        # check the form is valid
        if not request.form.get("name") or not request.form.get("email") or not request.form.get("message"):
            return "please fill out all required fields"

        # insert the row
        c.execute("INSERT INTO contactus (name, email, message, phone) VALUES (:name, :email, :message, :phone)", {"name": request.form.get("name"), "email": request.form.get("email"), "message": request.form.get("message"), "phone": request.form.get("phone")})
        conn.commit()

        # return success
        return "sent successfully!"
    else:
        return render_template("contact-us.html")

@app.route("/")
def index():
    return redirect("/home")

if __name__ == '__main__':
    app.run()