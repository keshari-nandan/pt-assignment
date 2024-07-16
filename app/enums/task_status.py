from enum import Enum


class TaskStatus(str, Enum):
    TO_DO = 'To Do'
    IN_PROGRESS = 'In Progress'
    DONE = 'Done'

    @classmethod
    def values(cls):
        return list(map(lambda x: x.value, cls))

