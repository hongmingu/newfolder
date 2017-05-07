from django.db import models
from title.models import Title
from django.contrib.auth.models import User

from django.db.models.signals import pre_save
from django.utils.text import slugify

# Create your models here.
class Stash(models.Model):

    stashUser = models.ForeignKey(User)
    stashTitle = models.ForeignKey(Title)

    stashSlug = models.SlugField(unique=True)
    stashDescription = models.TextField(max_length=200)

    stashImage = models.ImageField(null=True, blank=True, width_field="stashWidth", height_field="stashHeight")
    stashWidth = models.IntegerField(default=0)
    stashHeight = models.IntegerField(default=0)

    stashCreatedAt = models.DateTimeField(auto_now_add=True)
    stashUpdatedAt = models.DateTimeField(auto_now=True)

    stashPro = models.PositiveIntegerField(default=0)
    stashCon = models.PositiveIntegerField(default=0)
    stashBlinded = models.SmallIntegerField(default=1)

    def __str__(self):
        return self.stashDescription



def create_slug(instance, new_slug=None):
    slug = slugify(instance.satshTitle)
    if new_slug is not None:
        slug = new_slug
    qs = Stash.objects.filter(slug=slug).order_by('-id')
    exists = qs.exists()
    if exists :
        new_slug = '%s-%s' %(slug, qs.first().id)
        return create_slug()(instance, new_slug=new_slug)
    return slug


def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)
    # slug = slugify(instance.stashTitle)
    # exists = Stash.objects.filter(slug=slug).exists()
    # if exists:
    #     slug = '%s-%s' %(slug, instance.id)
    # instance.slug = slug


pre_save.connect(pre_save_post_receiver, sender=Stash)