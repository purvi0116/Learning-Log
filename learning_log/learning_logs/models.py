from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Topic(models.Model):
	"""A class the user is learning about"""
	text = models.CharField(max_length = 200)
	date_added = models.DateTimeField(auto_now_add=True)
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	def __str__(self):
		"""Returns a string representation of the class"""
		return self.text

# https://stackoverflow.com/questions/10344197/how-does-djangos-meta-class-work			
class Entry(models.Model):
	"""Something specific learned about a topic"""
	topic = models.ForeignKey(Topic ,on_delete=models.CASCADE) #https://youtu.be/RV-49Q-Z0yw  on_delete =CASCADE when Topic i sdeleted then all its referneced models(herer entry ) also get deleted
	text = models.TextField()
	date_added	= models.DateTimeField(auto_now_add=True)	
	class Meta: 
		verbose_name_plural = 'entries'

	def __str__(self):
		"""Return a string representation of the model."""
		if len(self.text)<50:
			return self.text[:]
		return self.text[:50]+"..."	