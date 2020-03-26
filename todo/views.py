from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.utils import timezone
from .models import Todo
from django.http import Http404


is_complete = []
no_complete = []
def index(request):
    todoList = Todo.objects.all()
    is_complete = [todo for todo in todoList if todo.is_complete==2]
    print(is_complete)
    no_complete = [todo for todo in todoList if todo.is_complete==1]
    print(no_complete)
    context = {'is_complete':is_complete,'no_complete':no_complete}
    return render(request,'index.html',context)
def add(request):
    if request.method == "GET":
        return render(request,'createTodo.html')
    elif request.method == "POST":
        todo_id =request.POST.get("todo_id")
        content = request.POST.get('content')
        createtime = request.POST.get('createtime')
        if todo_id and content and createtime:
            id = int(todo_id)
            ids = [int(todo.todo_id) for todo in Todo.objects.all()]
            print(ids)
            if id in ids:
                return render(request,'createTodo.html',{'error_message':"Todo任务已存在"})
            else:
                Todo.objects.create(todo_id=id,content=content,createtime=timezone.now())
                return redirect('/todo/list/')
        else:
            return render(request,"createTodo.html",{'error_message':"表单字段不能为空"})
def select(request,todo_id):
    try:
        todo = Todo.objects.get(todo_id=int(todo_id))
    except Todo.DoesNotExist:
        raise Http404("Todo task {} does not exist".format(todo_id))
    context = {"data":todo}
    return render(request,"detail.html",context)
def delete(request,todo_id):
    try:
        Todo.objects.filter(todo_id=int(todo_id)).delete()
        return redirect('/todo/list/')

    except:
        return render(request, 'index.html', {'message': '删除失败'})
def complete(request,todo_id):
    Todo.objects.filter(todo_id=todo_id).update(is_complete=2)
    return redirect('/todo/list/')
