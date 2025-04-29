# To-Do List API

A RESTful API built with FastAPI to manage tasks in a To-Do list application. 

## Features

- Create, read, update, and delete tasks.
- Data persistence with PostgreSQL.
- Authentication (optional for future implementation).

## Setup

1. Clone the repository:
git clone https://github.com/your-username/todo-api.git

2. Create a virtual environment and install dependencies:
python -m venv venv source venv/bin/activate # On Windows, use venv\Scripts\activate pip install -r requirements.txt

3. Set up the environment variables by creating a `.env` file:
DB_USER=your_db_user
DB_PASSWORD=your_db_password 
DB_HOST=localhost 
DB_PORT=5432 
DB_NAME=todo_db

4. Run the app: uvicorn app.main:app --reload

5. Access the API at `http://127.0.0.1:8000`.


