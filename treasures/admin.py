from django.contrib import admin
from treasures.models import *
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class MyCustomUserAdmin(UserAdmin):
    model = CustomUser


admin.site.register(CustomUser, MyCustomUserAdmin)