from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^categorys/$', views.CategoryList.as_view(), name='category_list'),
]
