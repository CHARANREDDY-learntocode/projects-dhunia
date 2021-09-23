from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _
from .models import CustomUser
# Register your models here.


class CustomUserAdmin(UserAdmin):
    '''Define admin model for custom User model with no username field.'''
    fieldsets = (
        (None, {'fields':('email', 'password')}),
        (_('Personal Information'), {'fields':('first_name', 'last_name')}),
        (_('Permissons'), {'fields':('is_active', 'is_staff', 'is_superuser',)}),
        (_('Important Dates'), {'fields':('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'contact_number', 'password1', 'password2'),
        }),
    )
    list_display = ('first_name', 'contact_number', 'email', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)

admin.site.register(CustomUser, CustomUserAdmin)