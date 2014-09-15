from django.db import models
from django.core.urlresolvers import reverse
from django.contrib import admin



# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=255)	
	slug = models.SlugField(unique=True, max_length=255)
	body = models.TextField()
	created = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.title


### Admin

class PostAdmin(admin.ModelAdmin):
	search_fields = ["title"]

admin.site.register(Post, PostAdmin)
