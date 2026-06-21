from pydantic import BaseModel
from typing import Optional

# This defines what data user sends when CREATING a task
class TaskCreate(BaseModel):
    title: str                        # required - must be text
    description: Optional[str] = None # optional - can be empty
    status: str = "pending"           # optional - default is "pending"

# This defines what data API sends BACK to user
class TaskResponse(BaseModel):
    id: int
    title: str
    description: Optional[str]
    status: str