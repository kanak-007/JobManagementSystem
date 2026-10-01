# Job Management System

A web-based Job Management System developed using Django and MySQL. The system allows users to register, log in, explore job opportunities, apply for jobs, upload resumes, save jobs, and track application status. Administrators can manage jobs and applications through an administrative interface.

## Features

### User Features

* User Registration and Login
* User Logout
* Browse Available Jobs
* View Job Details
* Apply for Jobs
* Upload Resume
* View Submitted Applications
* Track Application Status
* Save Jobs
* View Saved Jobs
* User Dashboard
* Custom 404 Page

### Admin Features

* Admin Login
* Admin Dashboard
* Add New Jobs
* Edit Existing Jobs
* Delete Jobs
* Manage Job Listings
* View Job Applications
* View Application Details
* Update Application Status

## Technologies Used

* **Frontend:** HTML, CSS, JavaScript
* **Backend:** Django
* **Database:** MySQL
* **Programming Language:** Python
* **Version Control:** Git & GitHub

## Project Structure

```text
JobManagementSystem/
│
├── jobmanagement/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── jobportal/
│   ├── migrations/
│   ├── models.py
│   ├── views.py
│   ├── admin.py
│   └── apps.py
│
├── static/
│   ├── css/
│   │   └── style.css
│   └── images/
│       └── hero-job.png
│
├── templates/
│   ├── home.html
│   ├── login.html
│   ├── register.html
│   ├── job_details.html
│   ├── application_form.html
│   ├── my_applications.html
│   ├── saved_jobs.html
│   ├── manage_jobs.html
│   └── ...
│
├── manage.py
├── .gitignore
└── README.md
```

## Database

The project uses **MySQL** as the database.

Database name:

```text
job_management
```

The main application data includes:

* Jobs
* Users
* Applications
* Saved Jobs
* Application Status

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/kanak-007/JobManagementSystem.git
```

### 2. Navigate to the Project

```bash
cd JobManagementSystem
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

For Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 5. Install Django

```bash
pip install django
```

Install the MySQL database driver:

```bash
pip install mysqlclient
```

### 6. Configure MySQL

Create a MySQL database named:

```text
job_management
```

Update the database configuration in:

```text
jobmanagement/settings.py
```

### 7. Run Migrations

```bash
python manage.py migrate
```

### 8. Create an Admin User

```bash
python manage.py createsuperuser
```

Follow the instructions displayed in the terminal.

### 9. Run the Development Server

```bash
python manage.py runserver
```

Open the application in your browser:

```text
http://127.0.0.1:8000/
```

## Application Workflow

```text
User Registration
        ↓
User Login
        ↓
Browse Jobs
        ↓
View Job Details
        ↓
Apply for Job
        ↓
Upload Resume
        ↓
Application Submitted
        ↓
Admin Reviews Application
        ↓
Application Status Updated
        ↓
User Tracks Application Status
```

## GitHub

Repository:

https://github.com/kanak-007/JobManagementSystem

## Future Enhancements

* Job Search and Filtering
* Job Categories
* Company Profiles
* Email Notifications
* Advanced Admin Dashboard
* Job Recommendations
* Pagination
* User Profile Management
* Deployment on a Cloud Platform

## Author

**Kanak Pawar**

GitHub: https://github.com/kanak-007

## License

This project is developed for educational and project purposes.
