from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Vegan(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    comment = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Vegan, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment


    