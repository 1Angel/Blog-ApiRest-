from django.db import models
from django.contrib.auth.models import User
from users.models import Account
# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="user_post")
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Comentarios(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="user_comentario")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post_comentario")
    description = models.TextField(max_length=900)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description
