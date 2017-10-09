from django.db import models
from django.utils import timezone
# Create your models here.
#new code here


class Post(models.Model): #this line defines our model, it is an object
	author = models.ForeignKey('auth.user')#this is a link to another model
	title = models.CharField(max_length = 200)#to define the text with limited number of characters
	text = models.TextField()# this is for long text 
	created_date = models.DateTimeField(default = timezone.now)#this is date and time
	published_date = models.DateTimeField(blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title