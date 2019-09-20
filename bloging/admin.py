from django.contrib import admin
from . import models


class PageAdmin(admin.ModelAdmin):
    list_display = ['owner', 'name', 'picture', 'about']


admin.site.register(models.Blogs, PageAdmin)
