from django.db import models
from django.utils import timezone


class Post(models.Model):#start always with uppercase letter

	author = models.ForeignKey('auth.user',on_delete=models.CASCADE)
	title = models.CharField(max_length=200)#varhchar
	text = models.TextField()
	created_date = models.DateTimeField(default = timezone.now)
	published_date = models.DateTimeField(blank=True,null=True)

	def publish(self):#lowercase and underscores
		self.published_date = timezone.now()
		self.save()#afterall,a model is a database object
					#You gotta save it!

	def __str__(self):#dudner-double under
		return self.title


# Create your models here.
