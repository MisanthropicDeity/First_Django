from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from blog.models import Posts
from django.urls import path

urlpatterns= [
    path('',ListView.as_view(queryset = Posts.objects.all().order_by("-date")[:25],
            template_name="blog/blog.html")),
    #url(r'^(?P<pk>\d+)$', DetailView.as_view(model = Posts, template_name = "blog/post.html")),
    path('<int:pk>/',DetailView.as_view(model = Posts, template_name = "blog/post.html"))
]
