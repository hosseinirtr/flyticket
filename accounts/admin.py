from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class CustomUserAdmin(UserAdmin):
    list_display = ('national_id', 'phone_number', 'birth_date', 'gender', 'is_staff')
    search_fields = ('national_id', 'phone_number')
    ordering = ('national_id',)

    fieldsets = (
        (None, {'fields': ('national_id', 'password')}),
        ('Personal info', {'fields': ('phone_number', 'birth_date', 'gender')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('national_id', 'password1', 'password2', 'phone_number', 'birth_date', 'gender', 'is_staff', 'is_superuser'),
        }),
    )


admin.site.register(User, CustomUserAdmin)
