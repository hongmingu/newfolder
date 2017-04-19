from django.db import models
from django.contrib.auth.models import User



class Title(models.Model):
    titleUser = models.ForeignKey(User)
    titleText = models.TextField(max_length=160, unique=True)
    titleCreatedAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titleText
#
#
# @receiver(post_save, sender=Title)
# def create_contentrelationship(sender, instance, created, **kwargs):
#     if created:
#         ContentRelationship.objects.create(=instance)
#
# @receiver(post_save, sender=Title)
# def save_contentrelationship(sender, instance, **kwargs):
#     instance.contentrelationship.save()
