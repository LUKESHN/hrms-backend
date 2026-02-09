# hrms-backend
# HRMS Lite — Backend (FastAPI)

## 📌 Project Overview

This is the backend service for **HRMS Lite**, a lightweight Human Resource Management System that allows an admin to manage employee records and track daily attendance.

The backend is built using **FastAPI** and provides RESTful APIs for:

* Employee management
* Attendance tracking
* Data persistence using SQLite
* Proper validations and error handling

This API is publicly deployed and connected to the frontend application.

---

## 🛠️ Tech Stack Used

* Python
* FastAPI
* SQLAlchemy (ORM)
* SQLite Database
* Uvicorn (ASGI Server)
* Render (Deployment)

---

## ▶️ Steps to Run Locally

### 1. Clone the repository

```
git clone https://github.com/LUKESHN/hrms-backend.git
cd hrms-backend
```

### 2. Create virtual environment

```
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```
pip install -r requirements.txt
pip install "pydantic[email]"
```

### 4. Run the server

```
python -m uvicorn main:app --reload
```

### 5. Open in browser

```
http://127.0.0.1:8000/docs
```

---

## 🌐 Live Backend URL

https://hrms-backend-u4o0.onrender.com

---

## ⚠️ Assumptions / Limitations

* Single admin user (no authentication)
* SQLite used for simplicity
* No advanced HR features like payroll or leave management
* Render free plan may cause cold start delays
