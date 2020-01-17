from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Message(models.Model):
    title = models.CharField(max_length=150)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.CharField(max_length=50)
    content = models.TextField()
