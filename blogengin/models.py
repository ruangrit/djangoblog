from django.db import models
from django.core.urlresolvers import reverse
from django.contrib import admin
from django.forms import ModelForm



# Create your models here.
# Create Category 
class Category(models.Model):
	title = models.CharField(max_length=255)
	description = models.TextField()
	cid = models.AutoField(primary_key=True)
	
	def __unicode__(self):
		return self.title
# Create Post topic
class Post(models.Model):
	title = models.CharField(max_length=255)	
	slug = models.SlugField(unique=True, max_length=255)
	body = models.TextField(blank=True)
	created = models.DateTimeField(auto_now_add=True)
	cid = models.ForeignKey(Category)

	def __unicode__(self):
		return self.title

# Create Comment in post topic
class Comment(models.Model):
	post = models.ForeignKey(Post)
	body = models.TextField()
	created = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return unicode("%s: %s" % (self.post, self.body[:60]))

### Admin

class PostAdmin(admin.ModelAdmin):
	search_fields = ["title"]

admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(Category)

