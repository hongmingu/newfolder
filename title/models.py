from django.db import models
from django.contrib.auth.models import User


class Title(models.Model):
    titleText = models.TextField(max_length=160, unique=True)
    titleRelationship = models.OneToOneField('relationship.ContentRelationship', on_delete=models.CASCADE)

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
