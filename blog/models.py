from django.db import models
from django.urls import reverse
from django.utils import timezone

class Category(models.Model):
	name = models.CharField(max_length=100)
	tagline = models.TextField()
	is_open = models.BooleanField(default=True)
	ordering = models.PositiveSmallIntegerField()

	def get_absolute_url(self):
		return reverse('category_detail', kwargs={'pk':self.pk})

	def __str__(self):
		return self.name

class Post(models.Model):
	category = models.ForeignKey('blog.Category')
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def get_absolute_url(self):
		return reverse('post_detail', kwargs={'pk':self.pk})

	def __str__(self):
		return self.title
