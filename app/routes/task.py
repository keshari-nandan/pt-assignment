from app.config.security import get_current_user, oauth2_scheme
from app.schemas.task import CreateTaskRequest, UpdateTaskRequest
from fastapi import APIRouter, Depends, status, Request
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from app.config.database import get_session
from app.responses.task import TaskResponse
from app.services import task

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"],
    responses={404: {"description": "Not found"}},
    dependencies=[Depends(oauth2_scheme), Depends(get_current_user)]
)


@router.post("", status_code=status.HTTP_201_CREATED, response_model=TaskResponse)
async def create_task(data: CreateTaskRequest, session: Session = Depends(get_session), auth=Depends(get_current_user)):
    return await task.create_task(auth, data, session)


@router.put("/{task_id}", status_code=status.HTTP_200_OK, response_model=TaskResponse)
async def update_task(task_id: int, data: UpdateTaskRequest, session: Session = Depends(get_session), auth=Depends(get_current_user)):
    return await task.update_task(auth, task_id, data, session)


@router.delete("/{task_id}", status_code=status.HTTP_200_OK, response_model=TaskResponse)
async def delete_task(task_id: int, session: Session = Depends(get_session), auth=Depends(get_current_user)):
    task_instance = await task.delete_task(auth, task_id, session)
    return JSONResponse(f"Task {task_instance.title} deleted successfully.", status_code=status.HTTP_200_OK)


@router.get("/{task_id}", status_code=status.HTTP_200_OK, response_model=TaskResponse)
async def get_task_by_id(task_id: int, session: Session = Depends(get_session), auth=Depends(get_current_user)):
    return await task.get_task(auth, task_id, session)


@router.get("", status_code=status.HTTP_200_OK, response_model=list[TaskResponse])
async def get_all_user_task(request: Request, session: Session = Depends(get_session), auth=Depends(get_current_user)):
    return await task.get_all_tasks(auth, request, session)
