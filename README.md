# Django TodoList REST API

The Django TodoList project is a RESTful API for managing tasks. Users can create, update, delete, and prioritize tasks while also changing their status from pending to finished. Each user has access to their own tasks, ensuring privacy and control over their to-do lists.

## Technologies Used

- Django
- Django Rest Framework
- JWT (JSON Web Tokens) for authentication

## Project Structure

- `tasks` app: Contains the `Task` model, `TaskSerializer`, and class-based views for managing tasks.
- `users` app: Handles user registration using `UserRegisterView` and `UserSerializer`.
- Authentication is handled using JWTAuthentication.

## Features

- User Registration: Users can create accounts using the `UserRegisterView` and `UserSerializer`.
- Task Management: Users can create, update, and delete tasks.
- Task Prioritization: Users can assign priorities to tasks.
- Task Status: Users can change the status of tasks from pending to finished.
- Authentication: JWT is used for user authentication.

## API Endpoints

- `/api/task/`: List all tasks, create a new task.
- `/api/task/<int:pk>/`: Retrieve, update, or delete a task by ID.
- `/api/register/`: Register a new user.

### Authentication

- JWT (JSON Web Tokens) are used for authentication. To access protected endpoints, users must include an `Authorization` header with the format `Bearer <token>`.

### Example Requests

#### Register a User

```http
POST /api/register/
Content-Type: application/json

{
    "username": "newuser",
    "password": "newpassword",
    "email": "user@example.com"
}
```

<br>

#### Create a Task

```http
POST /api/tasks/
Content-Type: application/json

{
    "title": "title1",
    "description": "description1",
    "priority": "high",
    "status": "pending",
    "author": 1
}
```

<br>

#### Update a Task

```http
PUT /api/tasks/{task_id}
Content-Type: application/json

{
    "title": "update title1",
    "description": "update description1",
    "priority": "high",
    "status": "pending",
    "author": 1
}
```

<br>

#### Delete a Task

```http
DELETE /api/tasks/{taks_id}
Content-Type: application/json
```
