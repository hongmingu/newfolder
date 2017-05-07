from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from title.models import Title

class UserRelationship(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    descriptionpro = models.TextField(max_length=200, blank=True)
    # allow_set = models.ManyToManyField("self", related_name="allowee_set", symmetrical=False, through="Allow")

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_userrelationship(sender, instance, created, **kwargs):
    if created:
        UserRelationship.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_userrelationship(sender, instance, **kwargs):
    instance.userrelationship.save()


class Bridge(models.Model):
    user_Bridging = models.ForeignKey('UserRelationship', related_name="who_is_bridging", )
    user_Bridged = models.ForeignKey('UserRelationship', related_name="who_is_bridged", )
    created_at = models.DateTimeField(auto_now_add=True, )
    updated_at = models.DateTimeField(auto_now=True, )

    def __str__(self):
        return "%s bridged %s at %s" % (self.user_Bridging, self.user_Bridged, self.updated_at)

    class Meta:
        unique_together = (('user_Bridging', 'user_Bridged'),)


# class ContentRelationship(models.Model):
#     allow_set = models.ManyToManyField('UserRelationship', related_name="wdt_set", symmetrical=False, through="Wdt")
#     description = models.TextField(max_length=200, blank=True)
#
#     def __str__(self):
#         return self.descriptionc

class Title2(models.Model):
    titleUser = models.ForeignKey(User)
    titleText = models.TextField(max_length=160, unique=True)
    titleCreatedAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titleText

class ContentRelationship(models.Model):
    title = models.OneToOneField(Title, blank=True, null=True)
    title2 = models.OneToOneField('Title2', blank=True, null=True)
    description = models.TextField(max_length=200, blank=True)

    def __str__(self):
        return self.description

@receiver(post_save, sender=Title)
def create_contentrelationship(sender, instance, created, **kwargs):
    if created:
        ContentRelationship.objects.create(title=instance)

@receiver(post_save, sender=Title)
def save_contentrelationship(sender, instance, **kwargs):
    instance.contentrelationship.save()

@receiver(post_save, sender=Title2)
def create_contentrelationship(sender, instance, created, **kwargs):
    if created:
        ContentRelationship.objects.create(title2=instance)

@receiver(post_save, sender=Title2)
def save_contentrelationship(sender, instance, **kwargs):
    instance.contentrelationship.save()

class Flow(models.Model):
    user_Flowing = models.ForeignKey('UserRelationship', related_name="who_is_Flowing", )
    content_Flowed = models.ForeignKey('ContentRelationship', related_name="content_is_Flowed", )
    created_at = models.DateTimeField(auto_now_add=True, )
    updated_at = models.DateTimeField(auto_now=True, )

    def __str__(self):
        return "%s bridged %s at %s" % (self.user_Flowing, self.content_Flowed, self.updated_at)

    class Meta:
        unique_together = (('user_Flowing', 'content_Flowed'),)



#
# @receiver(pre_save, sender=Title)
# def create_contentrelationship(sender, instance, created, **kwargs):
#     if created:
#         ContentRelationship.objects.create(Title=instance)
#
# @receiver(pre_save, sender=Title)
# def save_contentrelationship(sender, instance, **kwargs):
#     instance.contentrelationship.save()

# class Wdt(models.Model):
#     user_wdt = models.ForeignKey('UserRelationship', related_name="who_is_allowing",)
#     content_wdt = models.ForeignKey('ContentRelationship', related_name="who_is_allowed",)
#     created_at = models.DateTimeField(auto_now_add=True,)
#     updated_at = models.DateTimeField(auto_now=True,)
#
#     def __str__(self):
#         return "%s follows %s at %s" %(self.user_wdt, self.content_wdt, self.updated_at)
#
#     class Meta:
#         unique_together = (('user_wdt', 'content_wdt'),)
#



# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     description = models.TextField(max_length=200, blank=True)
#     allow_set=models.ManyToManyField("self", related_name="allowee_set", symmetrical=False, through="Allow")

#
# class Basemodel(models.Model):
#     set = models.ManyToManyField(User, related_name="setset_set", symmetrical=False, through="Follow")
#     class Meta :
#         abstract = True
# #
#
# class Post_1(Basemodel):
#     post1 = models.CharField(max_length=50)
#
# class Post_2(Basemodel):
#     post2 = models.CharField(max_length=50)
#
#
# class Follow(models.Model):
#     follower = models.ForeignKey(User, related_name="who_is_allowing",)
#     followee = models.ForeignKey(Basemodel, related_name="who_is_allowed",)
#     created_at = models.DateTimeField(auto_now_add=True,)
#     updated_at = models.DateTimeField(auto_now=True,)
#
#     def __str__(self):
#         return "%s follows %s at %s" %(self.follower, self.followee, self.updated_at)

########################################################################
# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     description = models.TextField(max_length=200, blank=True)
#     allow_set=models.ManyToManyField("self", related_name="allowee_set", symmetrical=False, through="Allow")
#
# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#
# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()
#
# class Allow(models.Model):
#     user_allowing = models.ForeignKey(Profile, related_name="who_is_allowing",)
#     user_allowed = models.ForeignKey(Profile, related_name="who_is_allowed",)
#     created_at = models.DateTimeField(auto_now_add=True,)
#     updated_at = models.DateTimeField(auto_now=True,)
#
#     def __str__(self):
#         return "%s follows %s at %s" %(self.user_allowing, self.user_allowed, self.updated_at)
#
# class WhatDo(models.Model):
#     tag = models.SlugField()
#     content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
#     object_id = models.PositiveIntegerField()
#     content_object = GenericForeignKey('content_type', 'object_id')
#
#     def __str__(self):
#         return self.tag


# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     description = models.TextField(max_length=200, blank=True)
#     allow_set=models.ManyToManyField("self", related_name="allowee_set", symmetrical=False, through="Allow")
