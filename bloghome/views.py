from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment, Contact
from .forms import CommentForm, SearchForm, PostForm
from django.http import Http404
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage,\
											PageNotAnInteger
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from taggit.models import Tag
from django.db.models import Count
from django.http import HttpResponse
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib import messages


def post_list(request, tag_slug=None):
	post_list = Post.published.all()
	tag = None
	if tag_slug:
		tag = get_object_or_404(Tag, slug=tag_slug)
		post_list = post_list.filter(tags__in=[tag])

	# Get the newest post
	newest_post = Post.published.order_by('-publish').first()

    # Exclude the newest post from the regular post list
	post_list = post_list.exclude(pk=newest_post.pk)

	tags = Tag.objects.all()

	paginator = Paginator(post_list, 4)
	page_number = request.GET.get('page', 1)
	
	try:
		posts = paginator.page(page_number)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)
	except PageNotAnInteger:
		posts = paginator.page(1)


	form = SearchForm
	query = None
	results = []

	if 'query' in request.GET:
		form = SearchForm(request.GET)
		if form.is_valid():
			query = form.cleaned_data['query']
			results = Post.published.raw("SELECT * FROM bloghome_post WHERE MATCH (title, body) AGAINST (%s)", [query])

	context = {'newest_post': newest_post, 
				'posts': posts,
				'tag': tag, 
				'tags': tags,
				'form': form,
				'query': query,
				'results': results}
	return render(request, 'blog/list.html', context)

def post_detail(request, post, year, month, day):
	post = get_object_or_404(Post,
							status=Post.Status.PUBLISHED,
							slug=post,
							publish__year=year,
							publish__month=month,
							publish__day=day)
	users = User.objects.all()
	

	# all tags
	tags = Tag.objects.all()

	comments = post.Comments.filter(active=True)
	form = CommentForm()

	post_tags_ids = post.tags.values_list('id', flat=True)
	similar_posts = Post.published.filter(tags__in=post_tags_ids)\
										.exclude(id=post.id)
	similar_posts = similar_posts.annotate(same_tags=Count('tags'))\
										.order_by('-same_tags', '-publish')[:4]

	context = {'post': post,
				'user_profile': users,
				'comments': comments,
				'form': form,
				'tags': tags,
				'similar_posts': similar_posts,
				'users': users}
	return render(request, 'blog/detail.html', context)

@require_POST
@login_required
def post_comment(request, post_id):
	post = get_object_or_404(Post,
								id=post_id,
								status=Post.Status.PUBLISHED)
	comment = None
	# a comment was posted
	form =CommentForm(data=request.POST, user=request.user)
	if form.is_valid():
		comment = form.save(commit=False)
		comment.post = post
		comment.user = request.user
		comment.save()
	
	context = {'post': post,
				'form': form,
				'comment': comment}

	return render(request, 'blog/comment.html',
							context)

def post_search(request):
	form = SearchForm
	query = None
	results = []

	if 'query' in request.GET:
		form = SearchForm(request.GET)
		if form.is_valid():
			query = form.cleaned_data['query']
			results = Post.published.raw("SELECT * FROM bloghome_post WHERE MATCH (title, body) AGAINST (%s)", [query])

	paginator = Paginator(results, 4)
	page_number = request.GET.get('page', 1)
	
	try:
		posts = paginator.page(page_number)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)
	except PageNotAnInteger:
		posts = paginator.page(1)

	context = {'form': form,
				'query': query,
				'results': results}
	return render(request, 'blog/search.html', context)

@login_required
def create_post(request):
	form = PostForm()
	if request.method == 'POST':
		form = PostForm(request.POST, request.FILES)
		if form.is_valid():
			form.instance.author = request.user
			form.save()
			messages.success(request, 'Your new post was successfully added')
			return redirect('profile', request.user.username)
		else:
			messages.error(request, 'error occurred when saving your post')
	else: 
		form = PostForm(request.POST)

	context = {'form': form}
	return render(request, 'blog/add_post.html', context)

@login_required
def edit_post(request, post_id):
	post = get_object_or_404(Post, pk=post_id)
	
	if request.method == 'POST':
		form = PostForm(request.POST, request.FILES, instance=post)
		if form.is_valid():
			form.instance.author = request.user
			form.save()
			messages.success(request, 'Your post successfully edited')
		else:
			messages.error(request, 'error occurred when editing your post')
	else:
		 form = PostForm(instance=post)

	context = {'form': form, 'post': post}
	return render(request, 'blog/edit_post.html', context)

@login_required
def published_posts(request, user_name):
	user = get_object_or_404(User,
								username=user_name)

	posts = Post.objects.filter(author=user)
	# profile_url = reverse('blog:published_posts', kwargs={'user_name': user_name})

	if not posts.exists():
		messages.error(request, "You don't have any posts yet.")
		return redirect('blog:create_post')

	paginator = Paginator(posts, 4)
	page_number = request.GET.get('page', 1)
	
	try:
		posts = paginator.page(page_number)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)
	except PageNotAnInteger:
		posts = paginator.page(1)

	context = {'user': user,
				'posts': posts,}
	return render(request, 'blog/user_list_post.html', context)

def about(request):
	contact = Contact.objects.all()
	context = {'contacts': contact}
	return render(request, 'blog/about.html', context)

def contact(request):
	contact = Contact.objects.all()
	context = {'contacts': contact}
	return render(request, 'blog/contact.html', context)

