# 🎟️ Event Management System

A simple **Django-based Event Management System** that allows users to register, log in, and book events. Admins can manage users, bookings, and events via the Django admin panel.

---

## 🚀 Features

* **User Registration & Authentication**

  * Sign up with username, email, and password
  * Login & logout functionality

* **Booking System**

  * Add and view bookings
  * Booking details stored in the database
  * Admin can manage bookings in Django Admin

* **Admin Panel**

  * Manage users
  * Manage events and bookings

---

## 🛠️ Tech Stack

* **Backend:** Django (Python)
* **Frontend:** HTML, CSS (with Django templates)
* **Database:** SQLite (default, but can be changed)
* **Auth:** Django’s built-in authentication system

---

## 📂 Project Structure

```
eventmanage/
│── eventmanage/        # Main Django project settings
│── userapp/            # App for user registration & login
│── bookings/           # App for booking management
│── templates/          # HTML templates
│── static/             # Static files (CSS, JS, images)
│── db.sqlite3          # SQLite database
│── manage.py           # Django management script
```

---

## ⚙️ Installation & Setup

1. **Clone the repo**

   ```bash
   git clone https://github.com/your-username/event-management.git
   cd event-management
   ```

2. **Create & activate a virtual environment**

   ```bash
   python -m venv env
   source env/bin/activate   # On Mac/Linux
   env\Scripts\activate      # On Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create superuser (for admin panel)**

   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**

   ```bash
   python manage.py runserver
   ```

7. Open in your browser → `http://127.0.0.1:8000/`

---


---

## 🧑‍💻 Contributing

1. Fork the project
2. Create a feature branch (`git checkout -b feature-name`)
3. Commit your changes (`git commit -m "Add new feature"`)
4. Push to the branch (`git push origin feature-name`)
5. Open a Pull Request

---

## 📜 License

This project is licensed under the **MIT License**.
You’re free to use, modify, and distribute it.

---
