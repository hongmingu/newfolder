from django.contrib import admin
from info.models import Userprofile, Contentsprofile, Allow, Wdt
# Register your models here.
admin.site.register(Userprofile)
admin.site.register(Contentsprofile)
admin.site.register(Allow)
admin.site.register(Wdt)
