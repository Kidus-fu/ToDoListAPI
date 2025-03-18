To-Do List API

A simple To-Do List API built with Django REST Framework.

## Features

* Create, read, update, and delete (CRUD) to-do items
* Authentication and authorization support
* API endpoints for managing tasks
## Installation

1, Clone the repository:

```bash
git clone https://github.com/Kidus-fu/MemoEthiopia.git
cd MemoEthiopia
```

2, Create a virtual environment and activate it:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use     `venv\Scripts\activate`
```

3, Install dependencies:

```bash
pip install -r requirements.txt
```

4, Set up the database:

```bash
python manage.py migrate
```

5, Create a superuser:

```bash
python manage.py createsuperuser
```

6, Run the development server:

```bash
python manage.py runserver
```
## API Endpoints

| Method | URL                  | Description            |
|------- |----------------------|------------------------|
| GET    | `/admin/`        | List all to-do items   |
| GET    | `/api-v1/list/`        | List all to-do items   |
| GET    | `/api-v1/list/{id}/`   | Retrieve single item   |
| POST   | `/api-v1/list/`        | Create a new to-do     |
| PUT    | `/api-v1/list/{id}/`   | Update a to-do         |
| DELETE | `/api-v1/list/{id}/`   | Delete a to-do         |
| POST   | `/api-v1/signup/`          | User signup             |
| POST   | `/api-v1/token/`           | Obtain token pair       |
| POST   | `/api-v1/token/refresh/`   | Refresh token           |
| GET    | `/Docs/`                   | API documentation       |
