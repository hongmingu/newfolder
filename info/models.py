from django.db import models
from django.contrib.auth.models import User
from title.models import Title
from basic.models import Basic
from stash.models import Stash
from post.models import Post
from comment.models import Comment
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    userprofileImage = models.ImageField()
    userprofileDescription = models.TextField(max_length=100)
    userprofileCreatedAt = models.DateTimeField(auto_now_add=True)
    userprofileUpdatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'UserProfile : %s' % (self.user.username)

@receiver(post_save, sender=User)
def create_userprofile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

class PostProfile(models.Model):
    title = models.OneToOneField(Title, null=True, blank=True)
    basic = models.OneToOneField(Basic, null=True, blank=True)
    stash = models.OneToOneField(Stash, null=True, blank=True)
    post = models.OneToOneField(Post, null=True, blank=True)
    comment = models.OneToOneField(Comment, null=True, blank=True)
    description = models.TextField(max_length=100, blank=True, null=True)
    postprofileCreatedAt = models.DateTimeField(auto_now_add=True)
    postprofileUpdatedAt = models.DateTimeField(auto_now=True)
    #Do something to connect Post1 or Post2

@receiver(post_save, sender=Title)
def create_postprofile1(sender, instance, created, **kwargs):
    if created:
        PostProfile.objects.create(title=instance)

@receiver(post_save, sender=Basic)
def create_postprofile1(sender, instance, created, **kwargs):
    if created:
        PostProfile.objects.create(basic=instance)

@receiver(post_save, sender=Stash)
def create_postprofile1(sender, instance, created, **kwargs):
    if created:
        PostProfile.objects.create(stash=instance)

@receiver(post_save, sender=Post)
def create_postprofile2(sender, instance, created, **kwargs):
    if created:
        PostProfile.objects.create(post=instance)

@receiver(post_save, sender=Comment)
def create_postprofile1(sender, instance, created, **kwargs):
    if created:
        PostProfile.objects.create(comment=instance)

class Allow(models.Model):
    allowingUserProfile = models.ForeignKey(UserProfile)
    allowedUserProfile = models.ForeignKey(UserProfile)
    allowCreatedAt = models.DateTimeField(auto_now_add=True)
    allowUpdatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'allowing : %s, allowed : %s, UpdatedAt : %s, Created At : %s' % (self.allowingUserProfile, self.allowedUserProfile, self.allowUpdatedAt, self.allowCreatedAt)

    class Meta:
        unique_together = (('allowingUserProfile', 'allowedUserProfile'),)

class Wdt(models.Model):
    wdtUser = models.ForeignKey(UserProfile)
    wdtContents = models.ForeignKey(PostProfile)
    wdtCreatedAt = models.DateTimeField(auto_now_add=True)
    wdtUpdatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s has Wdted %s at %s_created : %s' % (self.wdtUser, self.wdtContents, self.wdtUpdatedAt, self.wdtCreatedAt)

    class Meta:
        unique_together = (('wdtUser', 'wdtContents'),)