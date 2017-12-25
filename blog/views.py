from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from .models import Category

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
