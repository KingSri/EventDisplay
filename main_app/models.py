from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User
from django.core.files import File
from urllib.request import urlopen
from tempfile import NamedTemporaryFile

# Create your models here.

class Event(models.Model):
    title = models.CharField(max_length=200)
    description= models.TextField()
    start_time= models.DateField()
    likes = models.ManyToManyField(User, related_name='likes', blank=True)
    photo = models.ImageField(default="default.png", blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.title

    def total_likes(self):
        return self.likes.count()

    def get_absolute_url(self):
        return reverse('detail', args=[self.id])


#Comments on Event
class Comment(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    content = models.TextField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add= True)

    class Meta:
        ordering = ['timestamp']

    def __str__(self):
        return '{}-{}'.format(self.event.title, str(self.user.username))


# Event Registration
#
# class Registration(models.model):
#
