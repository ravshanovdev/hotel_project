from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, UserSession


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['phone', 'first_name', 'last_name', 'user_type', 'status', 'is_staff']

    fieldsets = (
        (None, {'fields': ('phone', 'password')}),
        ('Shaxsiy',
         {'fields': ('first_name', 'last_name', 'city', 'district', 'email', 'birth_date', 'language', 'image')}),
        ('Rol', {'fields': ('user_type', 'staff_role', 'status')}),
        ('Biznes', {'fields': ('company', 'inn', 'stir', 'legal_address')}),
        ('Huquqlar', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone', 'password1', 'password2', 'user_type', 'is_staff'),
        }),
    )
    ordering = ['phone']
    search_fields = ['phone', 'first_name', 'last_name']


admin.site.register(UserSession)
