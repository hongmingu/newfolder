from django.db import models

# Create your models here.
class Stash(models.Model):
    stashDescription = models.TextField(max_length=200)
    stashImage = models.ImageField()
    stashCreatedAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.stashDescription
