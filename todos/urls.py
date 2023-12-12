from django.urls import path

from todos.views import todo_list_list,todo_detail,create_todo

urlpatterns = [
    path("create/",create_todo,name="todo_list_create"),
    path("",todo_list_list,name="todo_list_list"),
    path("<int:id>/",todo_detail,name="todo_list_detail"),

]
