from users.models import UserCustom
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.
admin.site.register(UserCustom, UserAdmin)