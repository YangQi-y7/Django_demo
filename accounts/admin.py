from django.contrib import admin
from .models import User
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Critical Information', {'fields': ['name', 'password', 'time']}),
        ('Others', {'fields': ['sex', 'email', 'image']}),
    ]
    list_display = ('name', 'sex', 'time')
    search_fields = ['name']
    list_filter = ['time']


admin.site.register(User, UserAdmin)
