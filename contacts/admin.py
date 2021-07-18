from django.contrib import admin
from .models import Contact
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'firstname', 'lastname', 'email', 'car_title','created_date')
    list_display_links = ('id', 'firstname', 'lastname')
    search_fields = ('firstname', 'lastname', 'email', 'car_title')
    list_per_page=20

admin.site.register(Contact, ContactAdmin)