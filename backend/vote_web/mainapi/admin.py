from django.contrib import admin
from .models import *

# Register your models here.

class ItemoAdmin(admin.ModelAdmin):
    list_display = ('name',)

class VoteAdmin(admin.ModelAdmin):
    list_display = ('voter_name',)

admin.site.register(Item,ItemoAdmin)
admin.site.register(Vote,VoteAdmin)
