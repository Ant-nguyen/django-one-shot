from django.shortcuts import render
from todos.models import TodoItem, TodoList

# Create your views here.
def todo_list_list(request):
    todo_lists = TodoList.objects.all()

    context = {
        "todo_lists":todo_lists
    }
    return render(request,"todos/todolists.html",context)
