from fastapi import APIRouter, HTTPException
from database import get_connection
from models import TaskCreate, TaskResponse
from typing import List

router = APIRouter()

# ✅ GET - fetch all tasks
@router.get("/tasks", response_model=List[TaskResponse])
def get_all_tasks():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks")
    tasks = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return tasks

# ✅ GET - fetch one task by id
@router.get("/tasks/{task_id}", response_model=TaskResponse)
def get_task(task_id: int):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks WHERE id = ?", (task_id,))
    task = cursor.fetchone()
    conn.close()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return dict(task)

# ✅ POST - create a new task
@router.post("/tasks", response_model=TaskResponse)
def create_task(task: TaskCreate):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO tasks (title, description, status) VALUES (?, ?, ?)",
        (task.title, task.description, task.status)
    )
    conn.commit()
    new_id = cursor.lastrowid
    cursor.execute("SELECT * FROM tasks WHERE id = ?", (new_id,))
    new_task = dict(cursor.fetchone())
    conn.close()
    return new_task

# ✅ PUT - update an existing task
@router.put("/tasks/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, task: TaskCreate):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE tasks SET title=?, description=?, status=? WHERE id=?",
        (task.title, task.description, task.status, task_id)
    )
    conn.commit()
    cursor.execute("SELECT * FROM tasks WHERE id = ?", (task_id,))
    updated = cursor.fetchone()
    conn.close()
    if not updated:
        raise HTTPException(status_code=404, detail="Task not found")
    return dict(updated)

# ✅ DELETE - delete a task
@router.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()
    return {"message": "Task deleted successfully"}