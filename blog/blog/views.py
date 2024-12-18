from django.shortcuts import render

from django.views.generic import ListView, DetailView
from .models import Post

class BlogListView(ListView):
    model = Post
    template_name = 'article_list.html'
    
class BlogDetailView(DetailView):
    model = Post
    template_name = 'article_detail.html'
# Create your views here.
