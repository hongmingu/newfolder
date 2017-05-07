from django.db import models
from django.contrib.auth.models import User
from title.models import Title
from base.models import Base
from stash.models import Stash
from post.models import Post
from comment.models import Comment
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.

class Userprofile(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    userprofileImage = models.ImageField(blank=True)
    userprofileDescription = models.TextField(max_length=100)
    userprofileCreatedAt = models.DateTimeField(auto_now_add=True)
    userprofileUpdatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'UserProfile : %s, Updated at : %s' % (self.user.username, self.userprofileUpdatedAt)

@receiver(post_save, sender=User)
def createUserprofile(sender, instance, created, **kwargs):
    if created:
        Userprofile.objects.create(user=instance)
@receiver(post_save, sender=User)
def saveUserprofile(sender, instance, **kwargs):
    instance.userprofile.save()

class Contentsprofile(models.Model):
    title = models.OneToOneField(Title, null=True, blank=True)
    basic = models.OneToOneField(Base, null=True, blank=True)
    stash = models.OneToOneField(Stash, null=True, blank=True)
    post = models.OneToOneField(Post, null=True, blank=True)
    comment = models.OneToOneField(Comment, null=True, blank=True)
    description = models.TextField(max_length=100, blank=True, null=True)
    postprofileCreatedAt = models.DateTimeField(auto_now_add=True)
    postprofileUpdatedAt = models.DateTimeField(auto_now=True)
    #Do something to connect Post1 or Post2

@receiver(post_save, sender=Title)
def createContentprofileForTitle(sender, instance, created, **kwargs):
    if created:
        Contentsprofile.objects.create(title=instance)
@receiver(post_save, sender=Title)
def saveContentsprofileForTitle(sender, instance, **kwargs):
    instance.contentsprofile.save()

@receiver(post_save, sender=Base)
def createContentsprofileForBasic(sender, instance, created, **kwargs):
    if created:
        Contentsprofile.objects.create(basic=instance)
@receiver(post_save, sender=Base)
def saveContentsprofileForBasic(sender, instance, **kwargs):
    instance.contentsprofile.save()

@receiver(post_save, sender=Stash)
def createContentsprofileForStash(sender, instance, created, **kwargs):
    if created:
        Contentsprofile.objects.create(stash=instance)
@receiver(post_save, sender=Stash)
def saveContentsprofileForStash(sender, instance, **kwargs):
    instance.contentsprofile.save()

@receiver(post_save, sender=Post)
def createContentsprofileForPost(sender, instance, created, **kwargs):
    if created:
        Contentsprofile.objects.create(post=instance)
@receiver(post_save, sender=Post)
def saveContentsprofileForPost(sender, instance, **kwargs):
    instance.contentsprofile.save()

@receiver(post_save, sender=Comment)
def createContentsprofileForComment(sender, instance, created, **kwargs):
    if created:
        Contentsprofile.objects.create(comment=instance)
@receiver(post_save, sender=Comment)
def saveContentsprofileForComment(sender, instance, **kwargs):
    instance.contentsprofile.save()

class Bridge(models.Model):
    bridgingUserProfile = models.ForeignKey(Userprofile, related_name='bridgingUserProfile')
    bridgedUserProfile = models.ForeignKey(Userprofile, related_name='bridgedUserProfile')
    bridgeCreatedAt = models.DateTimeField(auto_now_add=True)
    bridgeUpdatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'bridging : %s, bridged : %s, UpdatedAt : %s, Created At : %s' % (self.bridgingUserProfile, self.bridgedUserProfile, self.bridgeCreatedAt, self.bridgeUpdatedAt)

    class Meta:
        unique_together = (('bridgingUserProfile', 'bridgedUserProfile'),)

class Flow(models.Model):
    flowingUserProfile = models.ForeignKey(Userprofile)
    flowedContentsProfile = models.ForeignKey(Contentsprofile)
    flowCreatedAt = models.DateTimeField(auto_now_add=True)
    flowUpdatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'flowingUser : %s, flowedContent : %s, UpdatedAt : %s, CreatedAt : %s' % (self.flowingUserProfile, self.flowedContentProfile, self.flowCreatedAt, self.flowUpdatedAt)

    class Meta:
        unique_together = (('flowingUserProfile', 'flowedContentsProfile'),)