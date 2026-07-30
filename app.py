from flask import Flask, render_template
from config import Config
from extensions import db
from models.student import Student
from flask import request, redirect, url_for

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

@app.route("/")
def home():
    return render_template(
        "home.html",
        logged_in=False
    )

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/add", methods=["GET", "POST"])
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
def students():

    all_students = Student.query.all()

    return render_template(
        "students.html",
        students=all_students
    )


@app.route("/edit/<int:id>", methods=["GET", "POST"])
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
def delete_student(id):

    student = Student.query.get(id)

    db.session.delete(student)

    db.session.commit()

    return "Student Deleted!"



if __name__ == "__main__":
    with app.app_context():
        print("Tables:", db.metadata.tables.keys())
        db.create_all()
        print("Database created!")
    app.run(debug=True)