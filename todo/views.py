from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import TodoItem
# Create your views here.


def todoView(request):
	all_todo_items = TodoItem.objects.all()
	return render(request, 'todo.html',
				  {'all_items': all_todo_items})


def addTodo(request):
	'''This method adds a new Todo item'''
	# create a new todo item object
	c = request.POST['content']
	new_item = TodoItem(content = c)
	new_item.save()
	return HttpResponseRedirect('/todoView/')


def deleteTodo(request, todo_id):
	item_to_delete = TodoItem.objects.get(id=todo_id)
	item_to_delete.delete()
	return HttpResponseRedirect('/todoView/')