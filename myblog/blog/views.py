from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView


class PostListView(ListView):
    queryset = Post.objects.filter(status="published")
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'
# Список опубликованных статей
# def post_list(request):
#     # return render(request, 'blog/post/list.html')
#     posts = Post.objects.filter(status="published")
#     return render(request, 'blog/post/list.html', {'posts': posts})
def post_list(request):
    object_list = Post.objects.filter(status="published")
    paginator = Paginator(object_list, 3)  # 3 кол-во постов на странице
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # Если параметр страницы не является целым числом,
        # мы извлекаем первую страницу результатов
        posts = paginator.page(1)
    except EmptyPage:
        # Если этот параметр является числом, превышающим последнюю страницу
        # результатов, мы извлекаем последнюю страницу.
        posts = paginator.page(paginator.num_pages)
    return render(request,
                  'blog/post/list.html',
                  {'page': page,
                   'posts': posts})


# Подробнее о нашем посте
def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                             status='published',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    return render(request, 'blog/post/detail.html', {'post': post})
