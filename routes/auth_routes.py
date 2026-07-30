from flask import Flask, render_template
from config import Config
from extensions import db, login_manager
from models.student import Student
from flask import request, redirect, url_for
from models.user import User
from flask import request, redirect, url_for, flash
from flask_login import login_user,login_required, logout_user
from werkzeug.security import check_password_hash
from flask import Blueprint

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