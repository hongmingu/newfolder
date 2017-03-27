from django.db import models

# Create your models here.
class Comment(models.Model):
    commentText = models.TextField(max_length=200)
    commentCreatedAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.commentText