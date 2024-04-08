from django.urls import path
from . import views
from django.utils.translation import gettext_lazy as _

app_name = 'blog'

urlpatterns = [
	path('', views.post_list, name='post_list'),
	path('<int:year>/<int:month>/<int:day>/<slug:post>/',
							views.post_detail, name='post_detail'),
	path('<int:post_id>/comment/', 
							views.post_comment, name='post_comment'),
	path('tag/<slug:tag_slug>',
							views.post_list, name='post_list_by_tag'),
	path('search/', views.post_search, name='post_search'),
	path('add-post/', views.create_post, name='create_post'),
	path('edit-post/<int:post_id>', views.edit_post, name='edit_post'),
	path('posts/<str:user_name>', views.published_posts, name='published_posts'),
	path('about/', views.about, name='about'),
	path('contact/', views.contact, name='contact'),
]

