from datetime import datetime

from app.enums.task_status import TaskStatus
from fastapi.exceptions import HTTPException
from app.models import Task


async def create_task(auth, data, session):
    task_exist = session.query(Task).filter(Task.title == data.title, Task.user_id == auth.id).first()
    if task_exist:
        raise HTTPException(status_code=400, detail="Task with the same name already exists.")

    task = Task()
    task.title = data.title
    task.description = data.description
    task.status = TaskStatus.TO_DO
    task.user_id = auth.id
    task.updated_at = datetime.now()
    session.add(task)
    session.commit()
    session.refresh(task)
    return task


async def update_task(auth, task_id, data, session):
    task = session.query(Task).filter(Task.id == task_id, Task.user_id == auth.id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found.")
    if data.status not in TaskStatus.values():
        raise HTTPException(
            status_code=404,
            detail=f"Task status is invalid. Valid status are: {', '.join(TaskStatus.values())}")
    task.title = data.title
    task.description = data.description
    task.status = data.status
    task.user_id = auth.id
    task.updated_at = datetime.now()
    session.commit()
    session.refresh(task)
    return task


async def delete_task(auth, task_id, session):
    task = session.query(Task).filter(Task.id == task_id, Task.user_id == auth.id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found.")
    session.delete(task)
    session.commit()
    return task


async def get_task(auth, task_id, session):
    task = session.query(Task).filter(Task.id == task_id, Task.user_id == auth.id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found.")
    return task


async def get_all_tasks(auth, request, session):
    query = session.query(Task).filter(Task.user_id == auth.id)
    status = request.query_params.get('status', None)
    search_term = request.query_params.get('q', None)
    sort_by = request.query_params.get('sort', None)
    if status and status != 'all':
        query = query.filter(Task.status == status)
    if search_term:
        query = query.filter(Task.title.ilike(f'%{search_term}%'))
    if sort_by:
        sorts = sort_by.split(',')
        for sort in sorts:
            try:
                name, order = sort.split(':')
                column = getattr(Task, name)
            except Exception as e:
                column = order = None
            if column:
                order = order if order == 'asc' else order == 'desc'
                query = query.order_by(column.desc()) if order == 'desc' else query.order_by(column.asc())
    return query.all()
