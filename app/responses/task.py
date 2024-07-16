from app.responses.base import BaseResponse


class TaskResponse(BaseResponse):
    id: int
    title: str
    description: str | None = None
    status: str | None = None
