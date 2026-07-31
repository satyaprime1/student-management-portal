from flask import Flask, render_template
from config import Config
from extensions import db, login_manager
from models.student import Student
from flask import request, redirect, url_for
from models.user import User
from flask import request, redirect, url_for, flash
from flask_login import login_user,login_required, logout_user
from werkzeug.security import check_password_hash, generate_password_hash
from flask import Blueprint
from decorators import admin_required

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]


        user = User.query.filter_by(
            username=username
        ).first()


        if user and check_password_hash(
            user.password_hash,
            password
        ):

            login_user(user)

            return redirect(url_for("student.home"))


        else:
            flash("Invalid username or password")


    return render_template("login.html")


@auth_bp.route("/logout")
@login_required
def logout():

    logout_user()

    flash("Logged out successfully.", "success")

    return redirect(url_for("auth.login"))



@auth_bp.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":
        
        email = request.form["email"]
        if User.query.filter_by(email=email).first():
            flash("Email already exists")
            return redirect(url_for("auth.register"))
        username = request.form["username"]
        if User.query.filter_by(username=username).first():
            flash("Username already exists")
            return redirect(url_for("auth.register"))
        password = request.form["password"]
        confirm_password = request.form["confirm_password"]
        if(password != confirm_password):
            flash("Passwords do not match")
            return redirect(url_for("auth.register"))

        password_hash = generate_password_hash(password)

        new_user = User(
            username=username,
            email=email,
            password_hash=password_hash,
        )
        db.session.add(new_user)
        db.session.commit()
        flash("User registered successfully. Please log in.", "success")

    return render_template("register.html")