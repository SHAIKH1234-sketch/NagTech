from django.contrib import admin
from .models import AboutMe
# Register your models here.
class AboutMeAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('header',)}
    list_display=['header','slug','title']

admin.site.register(AboutMe,AboutMeAdmin)
