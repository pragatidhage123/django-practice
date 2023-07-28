from django.urls import path
from . import views

urlpatterns = [
    path("",views.login,name="login"),
    path("get-add-data/",views.get_add_data,name="get_add_data"),
    path("student-details/",views.all_data,name="all_data"),
    path("teacher-get-data/",views.teacher_get_data,name="teacher_get_data"),
    path("teacher-details/",views.all_teacher_data,name="all_teacher_data"),

    
    
]