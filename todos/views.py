from django.shortcuts import render,get_object_or_404,redirect
from todos.models import TodoItem, TodoList
from todos.forms import TodoForm,ItemForm
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

def edit_todo(request,id):
    todo = get_object_or_404(TodoList,id=id)
    if request.method =="POST":
        form = TodoForm(request.POST, instance = todo)
        if form.is_valid():
            obj=form.save()
            return redirect("todo_list_detail",obj.id)
    else:
        form = TodoForm(instance =todo)

    context={
        "form":form
    }
    return render(request,"todos/edit.html",context)


def delete_todo(request,id):
    todo = get_object_or_404(TodoList,id=id)
    if request.method == "POST":
        todo.delete()
        return redirect("todo_list_list")

    return render(request,"todos/delete.html")

def create_item(request):
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            new_item = form.save()
            return redirect("todo_list_detail",new_item.list.id)
    else:
        form = ItemForm()
    context ={
        "form":form
    }
    return render(request,"todos/createitem.html",context)
