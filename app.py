from flask import Flask, render_template
from config import Config
from extensions import db, login_manager
from models.student import Student
from flask import request, redirect, url_for
from models.user import User
from flask import request, redirect, url_for, flash
from flask_login import login_user,login_required, logout_user
from werkzeug.security import check_password_hash
from routes.student_routes import student_bp
from routes.auth_routes import auth_bp

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
login_manager.init_app(app)

login_manager.login_view = "auth.login"

app.register_blueprint(student_bp)
app.register_blueprint(auth_bp)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)