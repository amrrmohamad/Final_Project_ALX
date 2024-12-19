# 🎓 E-Learning Platform

A modern and responsive website for offering online courses, allowing users to search, enroll, and track their progress through various educational content. This platform is designed for both learners and instructors to create a seamless online learning experience.

## Draw DataBase:

![image](https://github.com/user-attachments/assets/45568572-cb2a-4a85-99da-723644c26be9)


## 🎯 Features

### **General Features**

1. **User Authentication:**
   - Secure login, sign up, and logout functionality.
2. **Responsive Design:**
   - Fully responsive across mobile, tablet, and desktop devices.

### **For Students:**

1. **User-Friendly Interface:**
   - Simple navigation to browse and search for courses.
2. **Detailed Course Pages:**
   - View in-depth course descriptions, learning materials, and progress.

### **For Instructors:**

1. **Instructor Dashboard:**
   - Manage course creation, updates, and enrolled students with a specialized dashboard.
2. **Add Course:**
   - Instructors can add new courses.

## 🛠️ Tech Stack

- **Backend:** Django (Python)
- **Frontend:** HTML, CSS, JavaScript
- **Database:** SQLite
- **Version Control:** Git/GitHub

## 🛠️ Installation & Setup

Step 1: Clone the Repository

```bash
    git clone https://github.com/amrrmohamad/X-Courses.git
    cd X-Courses
```

Step 2: Install Dependencies
    For Python (Django) backend:

```bash
    pip install -r requirements.txt
```

Step 3: Run the Application
    For Django (Python):

```bash
    python mange.py runserver
```

Step 5: Access the Website
    Open your browser and go to <http://localhost:5000> (Django).
   
## 🤝 Contributing

Feel free to submit pull requests or issues for improving the website. We welcome contributions to add new features, enhance the design, or fix bugs.

## 📦 Folder Structure

```bash
    Final_Project_ALX/
    │
    ├── /E_learning/            # Django project directory
    │   ├── /E_learning/        # Main app directory for courses
    │   │   ├── /migrations/    # Database migrations
    │   │   ├── /static/        # Static files (CSS, JS, images)
    │   │   ├── /templates/     # HTML templates
    │   │   ├── /models.py      # Django models (Course, User, etc.)
    │   │   ├── /views.py       # Views for handling requests and rendering templates
    │   │   ├── /urls.py        # URL patterns for the courses app
    │   │   └── /admin.py       # Django admin configuration
    │   │
    │   ├── /static/            # Global static files for the project
    │   ├── /templates/         # Global templates (base.html, etc.)
    │   ├── /settings.py        # Django settings (including database, installed apps, etc.)
    │   ├── /urls.py            # Global URL patterns for the project
    │   └── /wsgi.py            # WSGI application entry point
    │
    ├── db.sqlite3              # Database file (SQLite by default)
    ├── manage.py               # Django management script
    ├── README.md               # Readme file
    ├── AUTHOR                  # Author file
    ├── .gitignore              # Git ignore file
    └── requirements.txt        # Environment file for sensitive data (database credentials, etc.)
```

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Author

1. ** Amr Mohamad Bakr.
