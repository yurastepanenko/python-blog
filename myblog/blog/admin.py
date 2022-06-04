from django.contrib import admin
from .models import Post

# Отвечает за отображение в админке сайта
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')


# Подключаем к админке сайта
admin.site.register(Post, PostAdmin)