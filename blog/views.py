from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic.base import RedirectView
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.utils import timezone
from .models import Category
from .models import Post

@method_decorator(login_required, name='dispatch')
class CategoryList(ListView):
	model = Category
	context_object_name = 'categorys'

@method_decorator(login_required, name='dispatch')
class CategoryDetail(DetailView):
	model = Category
	context_object_name = 'category'

@method_decorator(login_required, name='dispatch')
class CategoryCreate(CreateView):
	model = Category
	fields = ['name', 'tagline', 'is_open', 'ordering']

@method_decorator(login_required, name='dispatch')
class CategoryUpdate(UpdateView):
	model = Category
	fields = ['name', 'tagline', 'is_open', 'ordering']

@method_decorator(login_required, name='dispatch')
class CategoryDelete(DeleteView):
	model = Category
	context_object_name = 'category'
	success_url = reverse_lazy('category_list')

class PostList(ListView):
	model = Post
	context_object_name = 'posts'

	def get_queryset(self):
		return Post.objects.filter(category__is_open=True).filter(published_date__lte=timezone.now()).order_by('-published_date')

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		if self.request.user.is_authenticated:
			context['categorys'] = Category.objects.all().order_by('ordering')
		else:
			context['categorys'] = Category.objects.filter(is_open=True).order_by('ordering')
		return context

class PostListByCategory(PostList):
	def get_queryset(self):
		return Post.objects.filter(category__pk=self.kwargs['pk']).filter(published_date__lte=timezone.now()).order_by('-published_date')

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['category'] = get_object_or_404(Category, pk=self.kwargs['pk'])
		return context

class PostDetail(DetailView):
	model = Post
	context_object_name = 'post'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		if self.request.user.is_authenticated:
			context['categorys'] = Category.objects.all().order_by('ordering')
		else:
			context['categorys'] = Category.objects.filter(is_open=True).order_by('ordering')
		p = get_object_or_404(Post, pk=self.kwargs['pk'])
		context['category'] = p.category
		return context

@method_decorator(login_required, name='dispatch')
class PostAdd(CreateView):
	model = Post
	fields = ['category', 'title', 'text']

	def form_valid(self, form):
		post = form.save(commit=False)
		post.author = self.request.user
		return super().form_valid(form)

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		if self.request.user.is_authenticated:
			context['categorys'] = Category.objects.all().order_by('ordering')
		else:
			context['categorys'] = Category.objects.filter(is_open=True).order_by('ordering')
		return context

@method_decorator(login_required, name='dispatch')
class PostUpdate(UpdateView):
	model = Post
	fields = ['category', 'title', 'text']

	def form_valid(self, form):
		post = form.save(commit=False)
		post.author = self.request.user
		return super().form_valid(form)

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		if self.request.user.is_authenticated:
			context['categorys'] = Category.objects.all().order_by('ordering')
		else:
			context['categorys'] = Category.objects.filter(is_open=True).order_by('ordering')
		return context

@method_decorator(login_required, name='dispatch')
class PostDraftList(ListView):
	model = Post
	context_object_name = 'posts'
	template_name = 'blog/post_draft_list.html'

	def get_queryset(self):
		return Post.objects.filter(published_date__isnull=True).order_by('-created_date')

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		if self.request.user.is_authenticated:
			context['categorys'] = Category.objects.all().order_by('ordering')
		else:
			context['categorys'] = Category.objects.filter(is_open=True).order_by('ordering')
		return context

@method_decorator(login_required, name='dispatch')
class PostPublish(RedirectView):
	permanent = False
	query_string = True
	pattern_name = 'post_detail'

	def get_redirect_url(self, *args, **kwargs):
		post = get_object_or_404(Post, pk=kwargs['pk'])
		post.publish()
		return super().get_redirect_url(*args, **kwargs)

@method_decorator(login_required, name='dispatch')
class PostDelete(DeleteView):
	model = Post
	context_object_name = 'post'
	success_url = reverse_lazy('post_list')

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		if self.request.user.is_authenticated:
			context['categorys'] = Category.objects.all().order_by('ordering')
		else:
			context['categorys'] = Category.objects.filter(is_open=True).order_by('ordering')
		return context
