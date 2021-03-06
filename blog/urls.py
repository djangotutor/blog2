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
	url(r'^drafts/$', views.PostDraftList.as_view(), name='post_draft_list'),
	url(r'^posts/(?P<pk>\d+)/publish/$', views.PostPublish.as_view(), name='post_publish'),
	url(r'^posts/(?P<pk>\d+)/remove/$', views.PostDelete.as_view(), name='post_remove'),
	url(r'^accounts/login/$', views.UserLoginView.as_view(), name='login'),
	url(r'^posts/(?P<pk>\d+)/comment/$', views.CommentAdd.as_view(), name='add_comment_to_post'),
	url(r'^comments/(?P<pk>\d+)/approve/$', views.CommentApprove.as_view(), name='comment_approve'),
	url(r'^comments/(?P<pk>\d+)/remove/$', views.CommentDelete.as_view(), name='comment_remove'),
]
