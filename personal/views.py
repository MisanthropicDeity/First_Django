from django.shortcuts import render
#from django.http import HttpResponse

def PersonalView(request):
	return render(request,'personal/home.html')
# Create your views here.

def Contact(request):
	return render(request, 'personal/basic.html', { 'content' : ['If you would like to contact me email me @ vidhujoshi31@gmail.com']})
	