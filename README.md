# StudyFlow AI

An intelligent student task manager designed to help university students organize assignments, track deadlines, and manage their academic workload.

## Project Description

StudyFlow AI aims to make academic task management easier by allowing students to organize assignments by course, monitor deadlines, and track completion status.

This repository contains the **Assignment 2 backend API prototype**. It uses Python, FastAPI, mock in-memory data, and Bearer token authentication.

## Current Features

- Retrieve assignments belonging to the authenticated user.
- Retrieve a specific assignment by ID.
- Create new assignments.
- Update existing assignments.
- Delete assignments.
- Filter assignments by course, status, and deadline.
- Paginate assignment lists.
- Authenticate users using mock Bearer tokens.
- Apply role-based access control for students and administrators.
- Return consistent success and error responses.
- Display project information through an HTML greeting endpoint.
- Provide interactive API documentation through Swagger UI.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Backend programming language |
| FastAPI | REST API framework |
| Pydantic | Request data validation |
| Uvicorn | ASGI development server |
| In-memory mock data | Temporary assignment storage |

## Project Structure

```text
studyflow-ai/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── auth.py
│   ├── data.py
│   ├── schemas.py
│   │
│   └── routes/
│       ├── __init__.py
│       ├── assignments.py
│       └── greeting.py
│
├── docs/
│   └── API_DOCUMENTATION.md
│
├── examples/
│   └── requests.http
│
├── README.md
├── CONTRIBUTORS.md
├── requirements.txt
└── .gitignore
```

## Installation and Setup

### Requirements

- Python 3.10 or later
- pip
- Git

### 1. Clone the repository

```bash
git clone https://github.com/Muhammadrabboni/studyflow-ai.git
cd studyflow-ai
```

### 2. Create a virtual environment

Windows PowerShell:

```powershell
python -m venv .venv
```

### 3. Activate the virtual environment

```powershell
.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```powershell
pip install -r requirements.txt
```

### 5. Start the API server

```powershell
uvicorn app.main:app --reload
```

The API will be available at:

`http://127.0.0.1:8000`

## Authentication

The API uses HTTP Bearer token authentication.

Include the token in the request header:

```http
Authorization: Bearer user-a-token
```

### Mock Users

| User | Token | Role |
|---|---|---|
| User A | `user-a-token` | user |
| User B | `user-b-token` | user |
| Administrator | `admin-token` | admin |

Regular users can manage only their own assignments. Administrators can manage all assignments.

**Note:** These tokens are for assignment demonstration and testing only. They are not production authentication credentials.

## API Endpoints

Base path: `/api/v1`

| Method | Endpoint | Description |
|---|---|---|
| GET | `/greeting` | Displays project information as HTML |
| GET | `/assignments` | Retrieves accessible assignments |
| GET | `/assignments/{id}` | Retrieves one assignment |
| POST | `/assignments` | Creates an assignment |
| PUT | `/assignments/{id}` | Updates an assignment |
| DELETE | `/assignments/{id}` | Deletes an assignment |

See [API Documentation](docs/API_DOCUMENTATION.md) for request examples, response formats, query parameters, authentication details, and HTTP status codes.

## Interactive API Documentation

After starting the server, open:

- **Swagger UI:** http://127.0.0.1:8000/docs
- **OpenAPI JSON:** http://127.0.0.1:8000/openapi.json
- **Project Greeting:** http://127.0.0.1:8000/api/v1/greeting

Swagger UI allows you to explore and test the API endpoints.

## Example Requests

The `examples/requests.http` file contains sample requests for:

- Retrieving assignments.
- Creating, updating, and deleting assignments.
- Filtering and pagination.
- Testing different user roles.
- Testing authentication and authorization.
- Testing invalid and nonexistent resources.

You can execute these requests in Visual Studio Code using the REST Client extension.

## Data Storage

This prototype uses in-memory mock data instead of a permanent database.

Initial assignment records are provided for User A and User B. Data changes are temporary and will be lost when the application restarts.

## Git Contribution Summary

To display the number of commits made by each contributor, run:

```bash
git shortlog -sn --all
```

The command summarizes commits by Git author. The actual output should be checked against the team's Git history.

### Team Contributions

See [CONTRIBUTORS.md](CONTRIBUTORS.md) for the team's assigned responsibilities.

## Project Scope

This version focuses on the backend API requirements of Assignment 2.

The original project proposal includes additional planned features such as persistent database storage, AI-powered study planning, and Telegram notifications. These are outside the scope of this prototype and are not implemented in this version.

## Team

- Muhammadrabboni Asoev
- Nariman Huseynov
- Emin Miftaliyev