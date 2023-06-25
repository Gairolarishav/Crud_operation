from django.contrib import admin
from mainapp.models import Item

# Register your models here.
class formadmin(admin.ModelAdmin):
    list_display=['name','lname','desc']

admin.site.register(Item,formadmin)
