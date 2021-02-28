"""Citas views definitions"""

from datetime import datetime

import pytz

from django.db import DatabaseError, transaction
from django.utils import timezone
from drf_yasg.utils import swagger_auto_schema
from rest_framework import filters, pagination, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

# from . import exceptions as ex
# from . import politicas as p
from . import serializers as srlzs

from depas.application import List_departments
from depas.infrastructure.repo.orm import DepartmentOrm


repo_departments = DepartmentOrm()

list_department_use_case = List_departments(repo_departments)


class DepartmentView(viewsets.ViewSet):

    @swagger_auto_schema(
        responses={
            status.HTTP_200_OK: srlzs.DepartmentSerializer(many=True),
        },
    )
    def list(self, request):
        """Lista los departments
        """

        # with transaction.atomic():
        data=[_.json() for _ in list_department_use_case()]
        print(data)
        serializer = srlzs.\
            DepartmentSerializer(
                data=data,
                many=True
            )

        serializer.is_valid()
        print(serializer.data)
        return Response(data, status=status.HTTP_200_OK)
