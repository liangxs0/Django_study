from django.contrib import admin
from .models import UserList, FileList

# Register your models here.

admin.site.register(UserList)
admin.site.register(FileList)