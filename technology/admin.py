from django.contrib import admin
from .models import Technology
# Register your models here.
class TechnologyAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('product_name',)}
    list_display=['product_name','slug','price','stock','catagory']
admin.site.register(Technology,TechnologyAdmin)
