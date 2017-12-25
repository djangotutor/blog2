from django.db import models
from django.urls import reverse

class Category(models.Model):
	name = models.CharField(max_length=100)
	tagline = models.TextField()
	is_open = models.BooleanField(default=True)
	ordering = models.PositiveSmallIntegerField()

	def get_absolute_url(self):
		return reverse('category_detail', kwargs={'pk':self.pk})

	def __str__(self):
		return self.name
