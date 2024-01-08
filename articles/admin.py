from django.contrib import admin
from .models import Article, Comment

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'created')
    list_filter = ('author', 'created', 'updated')
    search_fields = ('title', 'author', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    inlines = [CommentInline]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['pk', 'author', 'article']
    list_display_links = ['author', 'article']


