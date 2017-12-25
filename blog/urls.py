from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^categorys/$', views.CategoryList.as_view(), name='category_list'),
	url(r'^category/(?P<pk>\d+)/$', views.CategoryDetail.as_view(), name='category_detail'),
	url(r'^category/add/$', views.CategoryCreate.as_view(), name='category_add'),
	url(r'^category/(?P<pk>\d+)/edit/$', views.CategoryUpdate.as_view(), name='category_edit'),
	url(r'^category/(?P<pk>\d+)/delete/$', views.CategoryDelete.as_view(), name='category_delete'),
]
