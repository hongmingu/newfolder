from django.contrib import admin
from practice.models import PostProfile, Post1, Post2, UserProfile
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Post1)
admin.site.register(Post2)
admin.site.register(PostProfile)
