from django.shortcuts import render

from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from .models import Post
# Create your views here.

## postListView class definition
class PostListView(ListView):
    model= Post

#postCreateView class definition
class PostCreateaview(CreateView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:all")


#postDetailView class definition
class PostDetailView(DetailView):
    model = Post
    

#postUpdateView class definition
class PostUpdateView(UpdateView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:all")

#postDeleteView class definition
class PostDeleteView(DeleteView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:all")

