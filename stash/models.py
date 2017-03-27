from django.db import models
from title.models import Title
from django.contrib.auth.models import User

# Create your models here.
class Stash(models.Model):
    stashUser = models.ForeignKey(User)
    stashTitle = models.ForeignKey(Title)
    stashDescription = models.TextField(max_length=200)
    stashImage = models.ImageField()
    stashCreatedAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.stashDescription
