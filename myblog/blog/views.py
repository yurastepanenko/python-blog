from django.shortcuts import render, get_object_or_404
from .models import Post


# Список опубликованных статей
def post_list(request):
    # return render(request, 'blog/post/list.html')
    posts = Post.objects.filter(status="published")
    return render(request, 'blog/post/list.html', {'posts': posts})


# Подробнее о нашем посте
def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                             status='published',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    return render(request, 'blog/post/detail.html', {'post': post})
