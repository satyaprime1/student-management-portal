from flask import Flask, render_template
from config import Config
from extensions import db, login_manager
from models.student import Student
from flask import request, redirect, url_for
from models.user import User
from flask import request, redirect, url_for, flash
from flask_login import login_user,login_required, logout_user
from werkzeug.security import check_password_hash

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
login_manager.init_app(app)

login_manager.login_view = "login"

@app.route("/")
def home():
    return render_template(
        "home.html",
        logged_in=False
    )


@app.route("/about")
@login_required
def about():
    return render_template("about.html")

@app.route("/add", methods=["GET", "POST"])
@login_required
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



@app.route("/students")
@login_required
def students():

    all_students = Student.query.all()

    return render_template(
        "students.html",
        students=all_students
    )


@app.route("/edit/<int:id>", methods=["GET", "POST"])
@login_required
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


@app.route("/delete/<int:id>")
@login_required
def delete_student(id):

    student = Student.query.get(id)

    db.session.delete(student)

    db.session.commit()

    return "Student Deleted!"


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))



@app.route("/login", methods=["GET", "POST"])
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

            return redirect("/")


        else:
            flash("Invalid username or password")


    return render_template("login.html")



if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)