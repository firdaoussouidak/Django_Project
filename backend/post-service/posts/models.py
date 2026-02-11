from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    author_id = models.IntegerField()
    author_username = models.CharField(max_length=150, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

