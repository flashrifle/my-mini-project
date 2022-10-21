from django.contrib import admin
from .models import bbs
# Register your models here.

class bbsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'writer', 'create_at', 'update_at']
    list_display_links = ['id', 'title']
    list_per_page = 10

admin.site.register(bbs, bbsAdmin)