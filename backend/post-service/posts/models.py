from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=200)
    accroche = models.CharField(max_length=255, blank=True, verbose_name="Mot / Accroche")
    citation = models.TextField(blank=True, verbose_name="Citation")
    auteur_signature = models.CharField(max_length=255, blank=True, verbose_name="Auteur / Signature")
    handle = models.CharField(max_length=100, blank=True, verbose_name="@handle")
    image = models.ImageField(upload_to='posts/', blank=True, null=True, verbose_name="Image")
    content = models.TextField()
    style = models.CharField(max_length=20, default='style1')
    theme = models.CharField(max_length=20, default='bordeaux')
    bg = models.CharField(max_length=20, default='floral')
    author_id = models.IntegerField()
    author_username = models.CharField(max_length=150, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author_id = models.IntegerField()
    author_username = models.CharField(max_length=150, default='', null=True, blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Comment by {self.author.username} on {self.post.title}"
