from django.contrib import admin
from .models import ContentRelationship, Title2
# Register your models here.

# class AllowInline(admin.TabularInline):
#     model = Allow
#     fk_name = 'user_allowing'
#     fk_name = 'user_allowed'
#     extra = 2 # how many rows to show

# class UserRelationshipAdmin(admin.ModelAdmin):
#     inlines = (AllowInline,)


admin.site.register(ContentRelationship)
admin.site.register(Title2)
# admin.site.register(UserRelationship)


