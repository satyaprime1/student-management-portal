from flask import render_template
from decorators import admin_required
from extensions import db
from models.student import Student
from flask import request, redirect, url_for
from models.user import User
from flask import request, redirect, url_for, flash
from flask_login import login_user,login_required, logout_user
from werkzeug.security import check_password_hash
from flask import Blueprint


student_bp = Blueprint("student", __name__)

@student_bp.route("/")
def home():
    return render_template(
        "home.html",
        logged_in=False
    )

@student_bp.route("/add", methods=["GET", "POST"])
@login_required
@admin_required
def add_student():

    if request.method == "POST":

        name = request.form["name"]
        age = request.form["age"]
        branch = request.form["branch"]
        email = request.form["email"]


        student = Student(
            name=name,
            age=age,
            branch=branch,
            email=email
        )


        db.session.add(student)
        db.session.commit()


        return "Student Added!"

    return render_template("add_student.html")

@student_bp.route("/students")
@login_required
def students():

    all_students = Student.query.all()

    return render_template(
        "students.html",
        students=all_students
    )


@student_bp.route("/edit/<int:id>", methods=["GET", "POST"])
@login_required
@admin_required
def edit_student(id):

    student = Student.query.get(id)


    if request.method == "POST":

        student.name = request.form["name"]
        student.age = request.form["age"]
        student.branch = request.form["branch"]
        student.email = request.form["email"]


        db.session.commit()

        return "Updated Successfully"


    return render_template(
        "edit_student.html",
        student=student
    )

@student_bp.route("/delete/<int:id>")
@login_required
@admin_required
def delete_student(id):

    student = Student.query.get(id)

    db.session.delete(student)

    db.session.commit()

    return "Student Deleted!"


@student_bp.route("/about")
def about():
    return render_template("about.html")