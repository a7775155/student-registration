🎓 Student Registration System
📌 Overview

The Student Registration System is a web-based application built with Django, styled using Bootstrap, and powered by PostgreSQL.
It allows administrators to manage student information, including registration, updating details, viewing records, and assigning courses.
This system streamlines student data management and provides a clean user-friendly interface.

🚀 Features

➕ Register new students with personal and academic details

✏️ Update and manage student records

🔍 Search and filter student information

🗑️ Delete student profiles

📑 Enroll students in courses/programs

📂 PostgreSQL database for secure storage

🎨 Bootstrap UI for responsive and modern design

🛠️ Tech Stack

Backend: Django (Python)

Frontend: HTML, CSS, Bootstrap

Database: PostgreSQL

Tools: Git, VS Code/PyCharm, pgAdmin

📂 Project Structure
student_registration/
│── manage.py
│── README.md
│── requirements.txt
│── db.sqlite3 (if using default dev DB)
│── /student_registration   # Main project settings
│── /students               # App for student registration
│   │── models.py           # Database models
│   │── views.py            # Views/Controllers
│   │── urls.py             # Routes
│   │── templates/          # HTML templates (Bootstrap)
│   │── static/             # CSS, JS, images
│── /templates              # Base templates

⚙️ Installation & Setup
1️⃣ Clone Repository
git clone https://github.com/your-username/student-registration.git
cd student-registration

2️⃣ Create & Activate Virtual Environment
python -m venv venv
source venv/bin/activate   # On Mac/Linux
venv\Scripts\activate      # On Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Configure Database

Update settings.py with your PostgreSQL credentials:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'student_db',
        'USER': 'postgres',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

5️⃣ Run Migrations
python manage.py makemigrations
python manage.py migrate

6️⃣ Create Superuser
python manage.py createsuperuser

7️⃣ Start Development Server
python manage.py runserver


Visit 👉 http://127.0.0.1:8000/

📖 Usage

Login with the admin account created

Register new students using the form

View, edit, or delete student records

Assign courses/programs to students

Manage data through the Django Admin panel

📸 Screenshots (Optional)

Add screenshots of your registration form, student list, and admin panel here.

✅ Future Enhancements

Authentication & role-based access (Admin, Student, Faculty)

Course scheduling & timetable management

Online fee payment integration

Export reports (PDF/Excel)

API endpoints for mobile apps

👨‍💻 Author

Developed by [Ashenafi Abera]
📧 Contact: [ashenafiabera090@gmail.com
