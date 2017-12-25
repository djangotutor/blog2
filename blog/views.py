from django.views.generic.list import ListView
from .models import Category

class CategoryList(ListView):
	model = Category
