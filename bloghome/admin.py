from django.contrib import admin
from .models import Post, Comment, Contact

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	list_display = ['title', 'slug', 'author', 'publish', 'status']
	list_filter = ['status', 'created', 'publish', 'author']
	search_fields = ['title', 'body']
	prepopulated_fields = {'slug': ['title']}
	raw_id_fields = ['author']
	date_hierarchy = 'publish'
	ordering = ['status', 'publish']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
	list_display = ['post', 'user', 'created', 'active']
	list_filter = ['active', 'created', 'updated']
	search_fields = ['name', 'email', 'body'] 

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
	list_display = ['about', 'contact', 'created']

	