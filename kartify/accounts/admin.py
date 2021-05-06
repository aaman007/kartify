from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

User = get_user_model()


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ['id', 'username', 'email', 'first_name', 'last_name', 'is_active', 'is_staff']
    readonly_fields = ['last_login', 'date_joined']
    fieldsets = [
        [None, {'fields': ['username', 'password']}],
        [_('Personal info'), {'fields': ['first_name', 'last_name', 'email']}],
        [_('Permissions'), {
            'fields': ['is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'],
        }],
        [_('Important dates'), {'fields': ['last_login', 'date_joined']}]
    ]

