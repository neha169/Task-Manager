from fastapi import FastAPI
from database import create_table
from routes import router

# Create the app
app = FastAPI(title="Task Manager API")

# Create the database table when app starts
create_table()

# Connect all the routes
app.include_router(router)

# Home page
@app.get("/")
def home():
    return {"message": "Task Manager API is running! 🚀"}