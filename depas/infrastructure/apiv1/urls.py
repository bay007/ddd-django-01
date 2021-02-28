from django.urls import path

from . import views as v

listar = {"get": "list"}
crear = {"post": "create"}

obtener = {"get": "retrieve"}
eliminar = {"delete": "destroy"}
actualizar = {"put": "update"}
parchar = {"patch": "partial_update"}


urlpatterns = []

urlpatterns += [

    path(
        "",
        v.DepartmentView.as_view({**listar}),
        name="department-listar",
    )
]
