from django.contrib import admin
from .models import *


class SeaCruiseGroupAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_filter = ['title', 'slug', 'text']
    search_fields = ['title', 'slug', 'text']


admin.site.register(SeaCruiseGroup, SeaCruiseGroupAdmin)
