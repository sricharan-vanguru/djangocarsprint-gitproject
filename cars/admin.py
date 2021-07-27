from django.contrib import admin
from .models import Car,Order
from django.utils.html import format_html
# Register your models here.
class CarAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style ="border-radius: 50px;" />'.format(object.car_photo.url))
  
    thumbnail.short_description = 'Car image'

    list_display = ('id','thumbnail','car_title','color', 'model' , 'fuel_type' ,'price','is_featured',)
    list_display_links = ('id', 'thumbnail', 'car_title',)
    list_editable = ('is_featured',)
    search_fields = ('id', 'car_title', 'city', 'model', 'fuel_type', 'price',)
    list_filter = ('city','model','body_style','fuel_type')

admin.site.register(Car,CarAdmin)
admin.site.register(Order)