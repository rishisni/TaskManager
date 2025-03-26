Task Management API (Django + DRF)

This is a Task Management API built using Django and Django REST Framework (DRF). It allows users to create, assign, update, and complete tasks.
 Features

    User Management (CRUD operations)

    Task Management (CRUD operations)

    Assign tasks to multiple users

    Update task status (including marking as completed)

    Superadmin Creation for full control

Installation & Setup
1️ Clone the Repository

git clone git@github.com:rishisni/TaskManager.git
cd taskmanager

2️ Create a Virtual Environment & Activate

python3 -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate

3️ Install Dependencies

pip install -r requirements.txt

4️ Apply Migrations & Create Superadmin

python manage.py migrate
python manage.py createsuperuser  # Follow prompts to set username & password

5️ Run the Development Server

python manage.py runserver

The API will be available at:
 http://localhost:8000/api/
 API Endpoints
Method	Endpoint	                        Description

GET	     /api/users/	                    List all users
GET	     /api/users/{user_id}/	            Retrieve a specific user
PATCH	 /api/users/{user_id}/	            Update user details
DELETE	 /api/users/{user_id}/	            Delete a user
GET	     /api/tasks/	                    List all tasks
POST	 /api/tasks/	                    Create a new task
GET	     /api/tasks/{task_id}/	            Retrieve a specific task
PATCH	 /api/tasks/{task_id}/update/	    Update a task (status, title, etc.)
DELETE	 /api/tasks/{task_id}/	            Delete a task
POST	 /api/tasks/{task_id}/assign/	    Assign users to a task
GET	     /api/users/{user_id}/tasks/	    Get all tasks assigned to a user

Notes

    Superadmin Creation: You can create a superadmin using createsuperuser for managing tasks and users.

    Testing Locally: The API can be tested at http://localhost:8000/api/ using Postman or cURL.