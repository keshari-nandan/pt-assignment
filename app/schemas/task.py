from app.enums.task_status import TaskStatus
from pydantic import BaseModel


class CreateTaskRequest(BaseModel):
    title: str
    description: str | None = None
    
    
class UpdateTaskRequest(BaseModel):
    title: str
    description: str | None = None
    status: TaskStatus | None = None
    