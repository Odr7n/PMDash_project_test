from django.contrib import admin
from .models import *

# Register your models here.

# class DashboardAdmin(admin.ModelAdmin):
#     list_display = ['title', 'author', 'date']
#     list_filter = ['title', 'author', 'date']
#
#
# class TagAdmin(admin.ModelAdmin):
#     list_display = ['title', 'status']
#     list_filter = ['title', 'status']
#
# admin.site.register(Dashboard, DashboardAdmin)
# admin.site.register(Tag, TagAdmin)