"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from webapp.views import myView, addTodo, delTodo
from personal.views import PersonalView, Contact

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo/', myView),
    path('', include('personal.urls')),
    path('blog/', include('blog.urls')),
    path('todohome/', include('webapp.urls')),
    path('addTodo/', addTodo),
    path('delTodo/<int:todo_id>/', delTodo),
    #path('contact/', Contact ,name="Contact")


]
