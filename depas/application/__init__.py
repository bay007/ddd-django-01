
from typing import List
from depas.models import Department
from depas.domain import DepartmentRepo


class List_departments:
    def __init__(self, depa_repo: DepartmentRepo) -> None:
        self.depa_repo = depa_repo

    def __call__(self) -> List[Department]:
        return self.depa_repo.list()
