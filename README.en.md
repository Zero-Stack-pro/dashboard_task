# ZeroStack Dashboard

## Description

**ZeroStack Dashboard** is a modern web panel for project and task management, built with Django. The interface features a dark, stylish theme focused on usability, analytics, and automation. Suitable for both personal and team use.

## Main Features

- Manage projects and tasks (create, view, status, deadlines)
- Modern responsive design (dark theme, smooth shadows, rounded corners)
- Live-updating date and time block
- Automatic project switching every 3 seconds
- Analytics for the current project: total tasks, completed, overdue
- Tasks are color-coded by status (overdue, due today, completed)
- Responsive layout for mobile and desktop

## Quick Start

1. Clone the repository:
   ```bash
   git clone <your repository URL>
   cd ZeroStack_DashBoard
   ```
2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install django
   ```
4. Apply migrations:
   ```bash
   python manage.py migrate
   ```
5. Run the server:
   ```bash
   python manage.py runserver
   ```
6. Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.

## Technologies
- Python 3.9+
- Django 4/5
- Bootstrap 5, Bootstrap Icons
- jQuery (for dynamic UI)

## Why use this project?
- Fast and visual project/task management
- Visual control of progress and deadlines
- Real-time analytics for each project
- A convenient starting point for further customization (e.g., integration with other services, roles, notifications, etc.)

---

*Developed to demonstrate modern UI/UX and analytics approaches in Django projects.* 