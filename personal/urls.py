#from django.conf.urls import url

from mysite.urls import path 

from . import views

urlpatterns= [
    path('', views.PersonalView ,name="PersonalView"),
    path('contact/', views.Contact ,name="Contact")

]
