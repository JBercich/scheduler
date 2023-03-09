import uuid
from abc import ABC, abstractmethod


class Event(ABC):
    _id = uuid.uuid4()
    name: str
    deadline: int

    @property
    @abstractmethod
    def category(self):
        pass


class WorkEvent:
    category: str = "WORK"

    def __init__(self, name, deadline):
        self.name = name
        self.deadline = deadline


class StudyEvent:
    category: str = "STUDY"

    def __init__(self, name, deadline):
        self.name = name
        self.deadline = deadline


class ActiveEvent:
    category: str = "ACTIVE"

    def __init__(self, name, deadline):
        self.name = name
        self.deadline = deadline
