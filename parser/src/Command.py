from abc import ABC, abstractmethod
from src.DrawState import DrawState


class Command(ABC):
    def __init__(self, name: str, args: list = None):
        self.name = name
        self.args = args if args is not None else []

    def __str__(self):
        return f"Command(name={self.name}, args={self.args})"

    def __repr__(self):
        return self.__str__()

    @abstractmethod
    def exec(self, ds: DrawState):
        pass
