from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import TodoListItem
def todoappView(request):
    all_todo_items = TodoListItem.objects.all()
    return render(request, 'todolist.html',
    {'all_items':all_todo_items})

def addTodoView(request):
    x = request.POST['content']
    y = request.POST['day']
    new_item = TodoListItem(content = x,day = y)
    new_item.save()
    return HttpResponseRedirect('/todoapp/')

def deleteTodoView(request, i):
    y = TodoListItem.objects.get(id= i)
    y.delete()
    return HttpResponseRedirect('/todoapp/')
    
def updateTodoView(request, i):
    x = request.POST['content']
    y = request.POST['day']
    z = TodoListItem.objects.get(id= i)
    new_item = TodoListItem(z.id, content = x,day = y)
    new_item.save()
    return HttpResponseRedirect('/todoapp/')
	
