# 📝 Django To-Do Application

A simple and clean To-Do management application built with **Django 5**.  
Users can log in, create tasks, add to-do items under each task, mark them as completed, edit, and delete tasks.

---

## 🚀 Features

### 🔐 Authentication
- Login system using Django's built-in authentication.
- Protected routes: all pages except `/login` require authentication.
- Logout option.

### 📌 Headings (Task Groups)
- Create new tasks.
- Display all tasks on the dashboard.
- Delete a task (removes all associated todos).

### ✅ To-Do Items
- Add todos under a task.
- Edit todos.
- Delete todos.
- Mark todos as *Completed*.
- Automatically separated into:
  - **Pending Tasks**
  - **Completed Tasks**

### 🎨 UI/UX
- Custom CSS styling inside templates.
- Modern clean layout.
- “Back” button on all pages except dashboard.

### Create and activate virtual environment
- python3 -m venv venv
- source venv/bin/activate   # macOS / Linux
- venv\Scripts\activate      # Windows

### pip install -r requirements.txt
- pip install -r requirements.txt

### Run migrations
- python manage.py migrate

### Create a superuser (optional)
- python manage.py createsuperuser

### Start the server
- python manage.py runserver

Go to http://127.0.0.1:8000/login/ to log in.

## Default URLs
| Page            | URL                                |
|-----------------|-------------------------------------|
| Login           | `/login/`                           |
| Dashboard       | `/`                                 |
| Create Heading  | `/heading/create/`                  |
| View Heading    | `/heading/<id>/`                    |
| Add To-Do       | `/todo/<heading_id>/create/`        |
| Edit To-Do      | `/todo/<todo_id>/edit/`             |
| Delete To-Do    | `/todo/<todo_id>/delete/`           |
| Complete To-Do  | `/todo/<todo_id>/complete/`         |
| Logout          | `/logout/`                          |
