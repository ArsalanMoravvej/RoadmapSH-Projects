# TaskTrackerAPI Documentation

## Overview

TaskTrackerAPI is a FastAPI-based application for managing tasks. It provides endpoints for user registration, authentication, and task management, including creating, updating, retrieving, and deleting tasks.

## Authentication

### POST /login

Authenticate a user and return a JWT token.

**Request:**

```json
{
  "username": "user@example.com",
  "password": "password123"
}
```

**Response:**

```json
{
  "access_token": "jwt_token",
  "token_type": "bearer"
}
```

## Users

### POST /users

Create a new user.

**Request:**

```json
{
  "name": "John Doe",
  "email": "john.doe@example.com",
  "password": "password123"
}
```

**Response:**

```json
{
  "id": 1,
  "name": "John Doe",
  "email": "john.doe@example.com",
  "created_at": "2023-10-01T12:00:00Z"
}
```

## Tasks

### GET /tasks

Retrieve all tasks with optional filtering, pagination, and search.

**Request Parameters:**

- `limit` (int, optional): Number of tasks to retrieve per page (default: 10)
- `page` (int, optional): Page number to retrieve (default: 1)
- `search` (str, optional): Search query to filter tasks by title

**Response:**

```json
{
  "data": [
    {
      "id": 1,
      "title": "Task 1",
      "description": "Description of Task 1",
      "status": 1,
      "priority": 5,
      "owner_id": 1,
      "owner": {
        "id": 1,
        "name": "John Doe",
        "email": "john.doe@example.com",
        "created_at": "2023-10-01T12:00:00Z"
      },
      "last_modified_at": null,
      "created_at": "2023-10-01T12:00:00Z"
    }
  ],
  "total": 1,
  "page": 1,
  "limit": 10
}
```

### GET /tasks/{id}

Retrieve a specific task by its ID.

**Request Parameters:**

- `id` (int): Task ID

**Response:**

```json
{
  "id": 1,
  "title": "Task 1",
  "description": "Description of Task 1",
  "status": 1,
  "priority": 5,
  "owner_id": 1,
  "owner": {
    "id": 1,
    "name": "John Doe",
    "email": "john.doe@example.com",
    "created_at": "2023-10-01T12:00:00Z"
  },
  "last_modified_at": null,
  "created_at": "2023-10-01T12:00:00Z"
}
```

### POST /tasks

Create a new task.

**Request:**

```json
{
  "title": "New Task",
  "description": "Description of the new task",
  "status": 1,
  "priority": 5
}
```

**Response:**

```json
{
  "id": 2,
  "title": "New Task",
  "description": "Description of the new task",
  "status": 1,
  "priority": 5,
  "owner_id": 1,
  "owner": {
    "id": 1,
    "name": "John Doe",
    "email": "john.doe@example.com",
    "created_at": "2023-10-01T12:00:00Z"
  },
  "last_modified_at": null,
  "created_at": "2023-10-01T12:00:00Z"
}
```

### DELETE /tasks/{id}

Delete a task by its ID.

**Request Parameters:**

- `id` (int): Task ID

**Response:**

```json
{
  "detail": "Task deleted successfully"
}
```

### PUT /tasks/{id}

Update a task by its ID.

**Request Parameters:**

- `id` (int): Task ID

**Request:**

```json
{
  "title": "Updated Task",
  "description": "Updated description of the task",
  "status": 2,
  "priority": 3
}
```

**Response:**

```json
{
  "id": 1,
  "title": "Updated Task",
  "description": "Updated description of the task",
  "status": 2,
  "priority": 3,
  "owner_id": 1,
  "owner": {
    "id": 1,
    "name": "John Doe",
    "email": "john.doe@example.com",
    "created_at": "2023-10-01T12:00:00Z"
  },
  "last_modified_at": "2023-10-01T12:30:00Z",
  "created_at": "2023-10-01T12:00:00Z"
}
```

### PATCH /tasks/{id}/status

Update a task's status by its ID.

**Request Parameters:**

- `id` (int): Task ID

**Request:**

```json
{
  "status": 3
}
```

**Response:**

```json
{
  "id": 1,
  "title": "Task 1",
  "description": "Description of Task 1",
  "status": 3,
  "priority": 5,
  "owner_id": 1,
  "owner": {
    "id": 1,
    "name": "John Doe",
    "email": "john.doe@example.com",
    "created_at": "2023-10-01T12:00:00Z"
  },
  "last_modified_at": "2023-10-01T12:30:00Z",
  "created_at": "2023-10-01T12:00:00Z"
}
```
