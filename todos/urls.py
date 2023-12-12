from django.urls import path

from todos.views import todo_list_list,todo_detail

urlpatterns = [
    path("",todo_list_list,name="todo_list_list"),
    path("<int:id>/",todo_detail,name="todo_list_detail")

]
