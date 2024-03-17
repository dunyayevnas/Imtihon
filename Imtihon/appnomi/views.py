from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView,DeleteView
from django.urls import reverse_lazy
from .models import Post


class BockListView(ListView):
    model = Post
    template_name = 'home.html'


class BlogDeletailView(DetailView):
    model = Post
    template_name = 'base_deletial.html'



class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title','author','body']
class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title','body']
class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')

# Create your views here.
