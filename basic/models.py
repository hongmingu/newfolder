from django.db import models
from title.models import Title
from django.contrib.auth.models import User

# Create your models here.
class Basic(models.Model):
    basicUser = models.ForeignKey(User)
    basicTitle = models.ForeignKey(Title)
    basicText = models.TextField(max_length=100)
    basicCreatedAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.basicText