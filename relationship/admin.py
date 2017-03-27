from django.contrib import admin
from .models import ContentRelationship, UserRelationship, Wdt, Allow
# Register your models here.

class AllowInline(admin.TabularInline):
    model = Allow
    fk_name = 'user_allowing'
    fk_name = 'user_allowed'
    extra = 2 # how many rows to show

class UserRelationshipAdmin(admin.ModelAdmin):
    inlines = (AllowInline,)


admin.site.register(ContentRelationship)
admin.site.register(Allow)
admin.site.register(Wdt)
admin.site.register(UserRelationship, UserRelationshipAdmin)

