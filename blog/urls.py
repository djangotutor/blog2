from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^categorys/$', views.CategoryList.as_view(), name='category_list'),
	url(r'^category/(?P<pk>\d+)/$', views.CategoryDetail.as_view(), name='category_detail'),
	url(r'^category/add/$', views.CategoryCreate.as_view(), name='category_add'),
	url(r'^category/(?P<pk>\d+)/edit/$', views.CategoryUpdate.as_view(), name='category_edit'),
	url(r'^category/(?P<pk>\d+)/delete/$', views.CategoryDelete.as_view(), name='category_delete'),
	url(r'^$', views.PostList.as_view(), name='post_list'),
	url(r'^categorys/(?P<pk>\d+)/$', views.PostListByCategory.as_view(), name='posts'),
	url(r'^posts/(?P<pk>\d+)/$', views.PostDetail.as_view(), name='post_detail'),
	url(r'^posts/new/$', views.PostAdd.as_view(), name='post_new'),
	url(r'^posts/(?P<pk>\d+)/edit/$', views.PostUpdate.as_view(), name='post_edit'),
]
