from django.shortcuts import render
from .models import Post

def post_list(request):
    posts = Post.objects.filter(created__isnull=False).order_by('created')
    return render(request, 'blog/post_list.html', {'posts': posts})
