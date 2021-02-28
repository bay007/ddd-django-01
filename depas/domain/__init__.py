
import abc
from dataclasses import dataclass
from typing import List


@dataclass
class Department:
    id: int
    title: str

    def json(self):
        return {
            "id": self.id,
            "title": self.title
        }


class DepartmentRepo(abc.ABC):
    @abc.abstractmethod
    def list(self) -> List[Department]: ...
