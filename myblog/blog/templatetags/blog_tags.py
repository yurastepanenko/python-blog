from django import template

register = template.Library()
from ..models import Post
from django.db.models import Count


# simple_tag: обрабатывает данные и возвращает строку
# inclusion_tag: обрабатывает данные и возвращает обработанный шаблон
# assignment_tag: обрабатывает данные и задает переменную в контексте


# @register.simple_tag(name='my_tag'). --зарегистрировать со своим именем
# кол-во постов
@register.simple_tag
def total_posts():
    return Post.objects.count()


@register.inclusion_tag('blog/post/latest_posts.html')
def show_latest_posts(count=5):
    latest_posts = Post.objects.order_by('-publish')[:count]
    return {'latest_posts': latest_posts}


@register.simple_tag
def get_most_commented_posts(count=5):
    return Post.objects.annotate(total_comments=Count('comments')). \
               order_by('-total_comments')[:count]
