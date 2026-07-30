from extensions import db


class Student(db.Model):

    __tablename__ = "students"


    id = db.Column(
        db.Integer,
        primary_key=True
    )


    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        unique=True
    )


    name = db.Column(
        db.String(100),
        nullable=False
    )


    age = db.Column(
        db.Integer
    )


    branch = db.Column(
        db.String(50)
    )


    email = db.Column(
        db.String(120),
        unique=True
    )

    user = db.relationship(
    "User",
    backref="student_profile",
    uselist=False
)