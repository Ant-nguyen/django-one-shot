from django.shortcuts import render,get_object_or_404,redirect
from todos.models import TodoItem, TodoList
from todos.forms import TodoForm
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

def create_todo(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            obj = form.save()
            return redirect("todo_list_detail",obj.id)

    else:
        form =TodoForm()

    context={
        "form":form
    }
    return render(request,"todos/create.html",context)
