# 🎓 Student Management Portal

A Student Management Portal built with **Flask**, **SQLAlchemy**, and **Bootstrap**. The application supports user authentication, role-based authorization, and complete CRUD operations for managing student records.

---

## 🚀 Features

### 👤 Authentication
- User Registration
- User Login
- User Logout
- Password Hashing using Werkzeug
- Session Management with Flask-Login

### 🔐 Authorization
- Role-Based Access Control (RBAC)
- Admin-only access for:
  - Add Student
  - Edit Student
  - Delete Student
- Students can view student records after logging in

### 📚 Student Management
- Add Student
- View Students
- Edit Student
- Delete Student

### 🎨 Frontend
- Bootstrap 5 UI
- Responsive Navigation Bar
- Flash Messages
- Jinja2 Templates

---

## 🛠️ Tech Stack

- Python
- Flask
- Flask-SQLAlchemy
- Flask-Login
- SQLite
- Bootstrap 5
- HTML5
- Jinja2

---

## 📂 Project Structure

```
Student-Management-Portal/
│
├── models/
│   ├── student.py
│   └── user.py
│
├── routes/
│   ├── student_routes.py
│   └── auth_routes.py
│
├── templates/
│   ├── base.html
│   ├── home.html
│   ├── students.html
│   ├── add_student.html
│   ├── edit_student.html
│   ├── login.html
│   ├── register.html
│   └── about.html
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
├── app.py
├── config.py
├── extensions.py
├── decorators.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/satyaprime1/Student-Management-Portal.git
cd Student-Management-Portal
```

### Create a virtual environment

```bash
python -m venv venv
```

### Activate the virtual environment

Windows

```bash
venv\Scripts\activate
```

Mac/Linux

```bash
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the application

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

## 👨‍💼 Default Admin Account

The application automatically creates an administrator account when run for the first time.

**Username**

```
admin
```

**Password**

```
admin123
```

---

## 📸 Current Features

- ✅ User Registration
- ✅ User Login
- ✅ User Logout
- ✅ Password Hashing
- ✅ Role-Based Authorization
- ✅ Admin Dashboard Access Control
- ✅ CRUD Operations
- ✅ SQLAlchemy ORM
- ✅ Flask Blueprints
- ✅ Responsive Bootstrap UI

---

## 🔮 Future Improvements

- Search Students
- Pagination
- Profile Management
- Email Verification
- Password Reset
- Dashboard Statistics
- Student Photo Upload
- REST API
- Docker Deployment

---

## 👨‍💻 Author

**Satya Harsha**

GitHub: https://github.com/satyaprime1

---

## 📄 License

This project is licensed under the MIT License.
