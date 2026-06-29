from django.urls import path
from . import views


urlpatterns=[
    path("",views.to_do_list,name='home'),
    path("delete/<int:id>/",views.to_do_delete,name="to_do_delete"),
    path("toggle/<int:id>/",views.to_do_toggle,name="to_do_toggle"),
]