from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Category

class CategoryList(ListView):
	model = Category
	context_object_name = 'categorys'

class CategoryDetail(DetailView):
	model = Category
	context_object_name = 'category'
