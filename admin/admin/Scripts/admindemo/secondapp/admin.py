from django.contrib import admin
from .models import Client

# Register your models here.

class ClientAdmin(admin.ModelAdmin):
    list_display=['c_name','c_email','c_contact','c_age','c_address']
    list_filter=['c_contact','c_age']

admin.site.register(Client,ClientAdmin)


