from django.db import models

class Category(models.Model):
	name = models.CharField(max_length=100)
	tagline = models.TextField()
	is_open = models.BooleanField(default=True)
	ordering = models.PositiveSmallIntegerField()

	def __str__(self):
		return self.name
