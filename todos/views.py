from django.shortcuts import render,get_object_or_404
from todos.models import TodoItem, TodoList

# Create your views here.
def todo_list_list(request):
    todo_lists = TodoList.objects.all()

    context = {
        "todo_lists":todo_lists
    }
    return render(request,"todos/todolists.html",context)


def todo_detail(request,id):
    details = get_object_or_404(TodoList,id=id)
    context ={
        "details": details
    }
    return render(request,"todos/tododetail.html",context)
