from django.db import models
from django.contrib.auth.models import User
from title.models import Title
from basic.models import Basic
from stash.models import Stash
from post.models import Post
# Create your models here.
class Comment(models.Model):

    commentBasic = models.ForeignKey(Basic, blank=True, null=True)
    commentStash = models.ForeignKey(Stash, blank=True, null=True)
    commentPost = models.ForeignKey(Post, blank=True, null=True)
    commentUser = models.ForeignKey(User)
    commentText = models.TextField(max_length=200)
    commentCreatedAt = models.DateTimeField(auto_now_add=True)
    commentUpdatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.commentText