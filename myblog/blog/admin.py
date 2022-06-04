from django.contrib import admin
from .models import Post


# Отвечает за отображение в админке сайта
class PostAdmin(admin.ModelAdmin):
    # Поля, которые будут отображаться
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    # raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']


# Подключаем к админке сайта
admin.site.register(Post, PostAdmin)