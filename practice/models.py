from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, primary_key=True)

@receiver(post_save, sender=User)
def create_userprofile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


class Post1(models.Model):
    text1 = models.TextField(max_length=110)
    #Do something to connect PostProfile

class Post2(models.Model):
    text2 = models.TextField(max_length=120)
    #Do something to connect PostProfile

class PostProfile(models.Model):
    post1 = models.OneToOneField(Post1, null=True, blank=True)
    post2 = models.OneToOneField(Post2, null=True, blank=True)
    description = models.TextField(max_length=100, blank=True, null=True)
    #Do something to connect Post1 or Post2

@receiver(post_save, sender=Post1)
def create_postprofile1(sender, instance, created, **kwargs):
    if created:
        PostProfile.objects.create(post1=instance)

@receiver(post_save, sender=Post2)
def create_postprofile2(sender, instance, created, **kwargs):
    if created:
        PostProfile.objects.create(post2=instance)

class bookmarkForPosts(models.Model):
    who_user = models.ForeignKey(UserProfile)
    what_bookmarked = models.ForeignKey(PostProfile)

'''
class UserProfile(models.Model):
    user = AutoOneToOneField(User, primary_key=True)

class Post1(models.Model):
    text1 = models.TextField(max_length=110)

class Post2(models.Model):
    text2 = models.TextField(max_length=120)

class bookmarkForPost1(models.Model):
    who_user = models.ForeignKey(UserProfile)
    what_bookmarked = models.ForeignKey(Post1)

class bookmarkForPost2(models.Model):
    who_user = models.ForeignKey(UserProfile)
    what_bookmarked = models.ForeignKey(Post2)
'''

'''
from django.db import models
from django.contrib.auth.models import User
from annoying.fields import AutoOneToOneField

# Create your models here.
class UProfile(models.Model):
    user = AutoOneToOneField(User, primary_key=True)

    def __str__(self):
        return self.user.username

class Post1(models.Model):
    text1 = models.TextField(max_length=100)

    def __str__(self):
        return self.text1

class Post1Profile(models.Model):
    post1 = AutoOneToOneField(Post, primary_key=True)
    des1 = models.TextField(max_length=100)

    def __str__(self):
        return self.des1

class Post2(models.Model):
    text2 = models.TextField(max_length=100)

    def __str__(self):
        return self.text2

class Post2Profile(models.Model):
    post2 = AutoOneToOneField(Post2, primary_key=True)
    des2 = models.TextField(max_length=100)

    def __str__(self):
        return self.des2

class followship(models.Model):
    who_following = models.ForeignKey(User)
    who_followed = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True,)
    updated_at = models.DateTimeField(auto_now=True,)

    def __str__(self):
        return "%s follows %s" %(self.who_following, self.who_followed)

class bookmarkForPost1(models.Model):
    who_user = models.ForeignKey(UProfile)
    what_bookmarked = models.ForeignKey(Post1)
    created_at = models.DateTimeField(auto_now_add=True,)
    updated_at = models.DateTimeField(auto_now=True,)

    def __str__(self):
        return "%s bookmarked %s" % (self.who_user, self.what_bookmarked)


class bookmarkForPost1(models.Model):
    who_user = models.ForeignKey(UProfile)
    what_bookmarked = models.ForeignKey(Post1)
    created_at = models.DateTimeField(auto_now_add=True,)
    updated_at = models.DateTimeField(auto_now=True,)

    def __str__(self):
        return "%s bookmarked %s" % (self.who_user, self.what_bookmarked)

'''
'''
class UserProfile(models.Model):
    user = AutoOneToOneField(User, primary_key=True)

@receiver(post_save, sender=User)
def create_userprofile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


class Post1(models.Model):
    text1 = models.TextField(max_length=110)
    #Do something to connect PostProfile

class Post2(models.Model):
    text2 = models.TextField(max_length=120)
    #Do something to connect PostProfile

class PostProfile(models.Model):
    post1 = models.ForeignKey(Post1, null=True, blank=True)
    post2 = models.ForeignKey(Post2, null=True, blank=True)
    description = models.TextField(max_length=100, blank=True, null=True)
    #Do something to connect Post1 or Post2

@receiver(post_save, sender=Post1)
def create_postprofile1(sender, instance, created, **kwargs):
    if created:
        PostProfile.objects.create(post1=instance)

@receiver(post_save, sender=Post2)
def create_postprofile2(sender, instance, created, **kwargs):
    if created:
        PostProfile.objects.create(post2=instance)

class bookmarkForPosts(models.Model):
    who_user = models.ForeignKey(UserProfile)
    what_bookmarked = models.ForeignKey(PostProfile)
'''