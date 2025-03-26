# Task Management API (Django + DRF)

This is a **Task Management API** built using **Django** and **Django REST Framework (DRF)**. It provides a simple yet powerful system for managing users and tasks, allowing assignment, updates, and status tracking.

---

## Features

- **User Management** (Create, Read, Update, Delete)
- **Task Management** (Create, Read, Update, Delete)
- **Assign Tasks** to multiple users
- **Update Task Status** (including marking as completed)
- **Superadmin Creation** for full administrative control

---

## Installation & Setup

### 1. Clone the Repository
```sh
git clone git@github.com:rishisni/TaskManager.git
cd TaskManager

2. Create and Activate a Virtual Environment

python3 -m venv venv

venv\Scripts\activate  (Windows)

source venv/bin/activate (Mac/Linux:)

3. Install Dependencies

pip install -r requirements.txt

4.Apply Migrations & Create a Superadmin

python manage.py migrate
python manage.py createsuperuser  # Follow the prompts to set up credentials

5. Run the Development Server

python manage.py runserver

The API will be available at:
http://localhost:8000/api/


API Endpoints

Method	        Endpoint	                        Description
GET	            /api/users/	                        List all users
GET	            /api/users/{user_id}/	            Retrieve details of a specific user
PATCH	        /api/users/{user_id}/	            Update user details
DELETE	        /api/users/{user_id}/	            Delete a user
GET	            /api/tasks/	                        List all tasks
POST	        /api/tasks/	                        Create a new task
GET	            /api/tasks/{task_id}/	            Retrieve details of a specific task
PATCH	        /api/tasks/{task_id}/update/	    Update a task (status, title, etc.)
DELETE	        /api/tasks/{task_id}/	            Delete a task
POST	        /api/tasks/{task_id}/assign/	    Assign users to a task
GET	            /api/users/{user_id}/tasks/	        Get all tasks assigned to a specific user


Additional Notes

    Superadmin Creation: You can create a superadmin using the createsuperuser command to manage tasks and users.

    Testing the API: The API can be tested using Postman or cURL at: http://localhost:8000/api/