from django.contrib import admin
from . import models


class PageAdmin(admin.ModelAdmin):
    list_display = [attr for attr in models.Blogs.__dict__.keys()] +\
                    ['id']#['id', 'owner', 'name', 'picture', 'about', 'subscribers']


admin.site.register(models.Blogs, PageAdmin)
