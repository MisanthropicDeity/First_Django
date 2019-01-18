from django.shortcuts import render
from django.http import HttpResponseRedirect
from . models import  TodoItem
from django.views.generic import TemplateView

class HomePageView(TemplateView):
	template_name = 'home.html'

def myView(request):
	all_todo_item = TodoItem.objects.all()

	return render(request,'todo.html',
		{'all_items':all_todo_item})
# Create your views here.
def addTodo(request):
	new_item = TodoItem(content = request.POST["content"])
	new_item.save()
	return HttpResponseRedirect('/todo/')

def delTodo(request,todo_id):
	TodoItem.objects.get(id=todo_id).delete()
	
	return HttpResponseRedirect('/todo/')
