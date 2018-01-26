from django.contrib import admin
from . import models


class PageAdmin(admin.ModelAdmin):
    list_display = ['id', 'owner', 'name', 'picture', 'about', 'subscribers']


admin.site.register(models.Blogs, PageAdmin)
