from django.contrib import admin
from . models import *
# Register your models here.

class categoryAdmin(admin.ModelAdmin):
    list_display=['name','slug']
    prepopulated_fields={'slug': ('name',)}
    
admin.site.register(category,categoryAdmin)

class productAdmin(admin.ModelAdmin):
    list_display=['name','slug','image','categorys','price','created']
    list_editable=['categorys','price']
    list_per_page=20
    prepopulated_fields={'slug': ('name',)}
admin.site.register(product,productAdmin)

admin.site.register(comment)
