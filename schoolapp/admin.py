from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin

from schoolapp.models import CustomUser

#blank UserModel for password encryption
class UserModel(UserAdmin):
    pass

admin.site.register(CustomUser,UserModel)