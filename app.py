from flask import Flask

from config import Config
from extensions import db, login_manager

from models.user import User

from werkzeug.security import generate_password_hash

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
    return db.session.get(User, int(user_id))


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        if not User.query.filter_by(username="admin").first():
            admin_user = User(
                username="admin",
                email="admin@example.com",
                password_hash=generate_password_hash("admin123"),
                role="admin"
            )
            db.session.add(admin_user)
            db.session.commit()

    app.run(debug=True)