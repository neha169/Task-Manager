# Task Manager REST API

A fully functional CRUD REST API built with **Python**, **FastAPI**, and **SQLite3**.

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python 3.x | Programming Language |
| FastAPI | Web Framework for building REST APIs |
| SQLite3 | Lightweight Database (built into Python) |
| Pydantic | Data Validation |
| Uvicorn | ASGI Server to run the app |

---

## 📁 Project Structure

```
task_manager/
│
├── main.py          # App entry point, starts the server
├── database.py      # SQLite3 database connection and table creation
├── models.py        # Pydantic models for request/response validation
└── routes.py        # All API endpoints (GET, POST, PUT, DELETE)
```

---

## ⚙️ Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/your-username/task-manager-api.git
cd task-manager-api
```

### 2. Install dependencies
```bash
pip install fastapi uvicorn
```

### 3. Run the application
```bash
uvicorn main:app --reload
```

### 4. Open Swagger UI to test APIs
```
http://127.0.0.1:8000/docs
```

---

## 📌 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/tasks` | Get all tasks |
| GET | `/tasks/{id}` | Get a single task by ID |
| POST | `/tasks` | Create a new task |
| PUT | `/tasks/{id}` | Update an existing task |
| DELETE | `/tasks/{id}` | Delete a task |

---

## 📝 Sample Request & Response

### Create a Task (POST /tasks)

**Request Body:**
```json
{
  "title": "Complete FastAPI project",
  "description": "Build and test all CRUD endpoints",
  "status": "pending"
}
```

**Response:**
```json
{
  "id": 1,
  "title": "Complete FastAPI project",
  "description": "Build and test all CRUD endpoints",
  "status": "pending"
}
```

---

### Update a Task (PUT /tasks/1)

**Request Body:**
```json
{
  "title": "Complete FastAPI project",
  "description": "Build and test all CRUD endpoints",
  "status": "done"
}
```

**Response:**
```json
{
  "id": 1,
  "title": "Complete FastAPI project",
  "description": "Build and test all CRUD endpoints",
  "status": "done"
}
```

---

## ✅ Features

- Full **CRUD** operations (Create, Read, Update, Delete)
- **Automatic database creation** on first run — no manual setup needed
- **Data validation** using Pydantic models
- **Error handling** with proper HTTP status codes (404 if task not found)
- **Auto-generated API documentation** via Swagger UI at `/docs`
- Clean, modular code structure following REST API best practices

---

## 🚀 Future Improvements

- Add JWT Authentication (Login / Register)
- Add user accounts so each user sees only their own tasks
- Deploy to cloud (Railway / Render) for a live URL
- Add due dates and priority levels to tasks

---

## 👩‍💻 Author

**Neha Nirmal**  
Backend Developer (Fresher)  
📧 nehanirmal1678@gmail.com  
🔗 [LinkedIn](https://linkedin.com/in/neha-nirmal-54a042216) | [GitHub](https://github.com/neha169)
