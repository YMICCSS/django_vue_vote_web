from django.contrib import admin
from .models import *

# Register your models here.


class ItemoAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Item,ItemoAdmin)
