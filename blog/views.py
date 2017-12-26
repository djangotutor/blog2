from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django.utils import timezone
from .models import Category
from .models import Post

class CategoryList(ListView):
	model = Category
	context_object_name = 'categorys'

class CategoryDetail(DetailView):
	model = Category
	context_object_name = 'category'

class CategoryCreate(CreateView):
	model = Category
	fields = ['name', 'tagline', 'is_open', 'ordering']

class CategoryUpdate(UpdateView):
	model = Category
	fields = ['name', 'tagline', 'is_open', 'ordering']

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
		context['categorys'] = Category.objects.filter(is_open=True).order_by('ordering')
		return context
