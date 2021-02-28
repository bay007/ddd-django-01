from django.db import models
from django.core.exceptions import ValidationError
from django.db.models.base import ModelStateFieldsCacheDescriptor
from django.utils.translation import gettext_lazy as _
from depas.domain import Department as D


def exclude_no_ascii_chars(value):
    if "ñ" in value or "Ñ" in value:
        raise ValidationError(
            _('Can\'t contain letter %(value)s in title'),
            params={'value': value},
        )


class Department(models.Model):
    @classmethod
    def from_domain(cls, department: D):
        _department = cls(
            id=D.id,
            title=D.title
        )
        _department.full_clean()
        return _department

    def to_domain(self) -> D:
        self.full_clean()
        _department = D(
            id=self.id,
            title=self.title
        )

        return _department

    title = models.CharField(
        max_length=100,
        validators=[
            exclude_no_ascii_chars
        ])

    class Meta:
        app_label = 'depas'


# class Employee(models.Model):
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     department = models.ForeignKey(Department, on_delete=models.PROTECT)
#     birthdate = models.DateField(null=True, blank=True)

#     class Meta:
#         app_label = 'depas'
