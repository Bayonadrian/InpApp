#django modules
from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin

class UserAdminConfig(UserAdmin):
    model = User
    search_fields = ('email', 'area', 'salary')
    list_filter = ('email', 'area', 'is_active', 'is_staff')
    ordering = ('-start_date',)
    list_display = ('email', 'area', 'salary', 'start_date',
                    'is_active', 'is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'area', 'position')}),
        ('Permisos', {'fields': ('is_staff', 'is_active', 'is_superuser')}),
        ('Informacion personal', {'fields': ('salary', 'start_date', 'user_name', 'last_name')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'user_name', 'last_name', 'start_date', 'area', 'position', 'salary','password1', 'password2', 'is_active', 'is_staff', 'is_superuser')}
         ),
    )


admin.site.register(User, UserAdminConfig)