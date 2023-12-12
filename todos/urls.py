from django.urls import path

from todos.views import todo_list_list,todo_detail,create_todo,edit_todo,delete_todo,create_item

urlpatterns = [
    path("items/create/",create_item,name="todo_item_create"),
    path("<int:id>/delete/",delete_todo,name= "todo_list_delete"),
    path("<int:id>/edit/",edit_todo,name="todo_list_update"),
    path("create/",create_todo,name="todo_list_create"),
    path("",todo_list_list,name="todo_list_list"),
    path("<int:id>/",todo_detail,name="todo_list_detail"),

]
