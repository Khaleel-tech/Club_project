# Student ERP for Club Management

A web-based ERP system built with Django for managing student club events, roles, and attendance.  
It supports three roles: **Superadmin**, **Mentor**, and **Student**.

---

## 📝 Description

This system allows:
- The **Superadmin** to create events and assign mentors.
- The **Mentor** to manage events and take student attendance.
- The **Student** to view events, register for them, and track their attendance.

---

## 💻 Tech Stack

- **Frontend**: HTML, CSS, GSAP  
- **Backend**: Django  
- **Database**: SQL

---

## 🚀 Features

- 🔐 User Authentication (Create Account, Login)
- 🧑‍🏫 Role-based Dashboards (Superadmin, Mentor, Student)
- 🗓️ Event Creation and Assignment
- ✅ Attendance Tracking by Mentors
- 📊 Student Dashboard to View Attendance and Registered Events

---

## ⚙️ Installation Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Khaleel-tech/Club_project.git
   cd Club_project
2. **Create a Virtual Environment**
   ```bash
   python -m venv venv
    # Activate it:
    # On Windows:
    venv\Scripts\activate
    # On macOS/Linux:
    source venv/bin/activate
3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
4. **Apply migrations**
   ```bash
   #before migrations don't forget to change the databasse configurations according to you in settings.py
    python manage.py makemigrations
    python manage.py migrate
5. **Run the Server**
   ```bash
   python manage.py runserver
6. **Open your browser at**
   http://127.0.0.1:8000/

   
---

## 🧑‍💻 Author

- **Khaleel**  
  [GitHub](https://github.com/Khaleel-tech) • [LinkedIn](https://www.linkedin.com/in/shaik-khasim-khaleel-basha-89b877278/)


---
## 📂 License
    This project is licensed for learning and development use. Customize it as needed.
