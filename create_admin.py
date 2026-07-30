from app import app
from extensions import db
from models.user import User
from werkzeug.security import generate_password_hash


with app.app_context():

    admin = User(
        username="admin",
        email="admin@gmail.com",
        password_hash=generate_password_hash("admin123"),
        role="admin"
    )

    db.session.add(admin)
    db.session.commit()

    print("Admin created successfully!")