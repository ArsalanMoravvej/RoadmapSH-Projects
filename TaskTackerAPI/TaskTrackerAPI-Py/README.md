# TaskTrackerAPI

TaskTrackerAPI is a FastAPI-based application for managing tasks. It provides endpoints for user registration, authentication, and task management, including creating, updating, retrieving, and deleting tasks.

## Features

- User registration and authentication
- Task management (CRUD operations)
- Soft deletion of tasks
- Pagination and search for tasks
- JWT-based authentication

## Project Structure

```
.
├── .env
├── alembic/
│   ├── env.py
│   ├── README
│   ├── script.py.mako
│   ├── versions/
│   │   ├── ...
├── alembic.ini
├── app/
│   ├── config.py
│   ├── database.py
│   ├── main.py
│   ├── models.py
│   ├── oauth2.py
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   ├── task.py
│   │   ├── user.py
│   ├── schemas.py
│   ├── utils.py
```

## Installation

1. Clone the repository:

```sh
git clone https://github.com/yourusername/TaskTrackerAPI.git
cd TaskTrackerAPI
```

2. Create and activate a virtual environment:

```sh
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. Install the dependencies:

```sh
pip install -r requirements.txt
```

4. Set up the environment variables:

Create a .env file in the root directory with the following content:

```env
DATABASE_HOSTNAME=The hostname of the database server.
DATABASE_PORT=The port number on which the database server is listening.
DATABASE_NAME=The name of the database to connect to.
DATABASE_USERNAME=The username to use for database authentication.
DATABASE_PASSWORD=The password to use for database authentication.
SECRET_KEY=The secret key used for cryptographic operations.
ALGORITHM=The algorithm used for token encoding.
ACCESS_TOKEN_EXPIRATON_MINUTES=The duration (in minutes) for which the access token is valid.
```

5. Run the database migrations:

```sh
alembic upgrade head
```

6. Start the FastAPI server:

```sh
uvicorn app.main:app --reload
```

## API Endpoints

### Authentication

- `POST /login`: User login

### Users

- `POST /users`: Create a new user

### Tasks

- `GET /tasks`: Retrieve all tasks with optional filtering, pagination, and search
- `GET /tasks/{id}`: Retrieve a specific task by its ID
- `POST /tasks`: Create a new task
- `DELETE /tasks/{id}`: Delete a task by its ID
- `PUT /tasks/{id}`: Update a task by its ID

## License

This project is licensed under the MIT License.
```

This content should be placed inside the README.md