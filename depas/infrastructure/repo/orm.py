

from typing import List
from depas.domain import DepartmentRepo, Department
from depas.models import Department as DepartmentModelORM


class DepartmentOrm(DepartmentRepo):

    def list(self) -> List[Department]:
        self._repo = DepartmentModelORM
        return [_.to_domain() for _ in self._repo.objects.all()]
