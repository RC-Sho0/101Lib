from django.contrib import admin
from django.db import models
from home.models import Users
from home.forms import RegistrationForm
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class UsersAdmin(UserAdmin):
    model = Users
    add_form = RegistrationForm
 
    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    ordering = ('email',)
    search_fields = ('email',)
 
    fieldsets = (
        (
            'User profile',
            {
                'fields': (
                    'first_name',
                    'last_name',
                    'email',
                    'username',
                    'password',
                    'birth_date',
                    'phone_number',
                    'ngaylapthe',
                    'ngayhethan',
                  
                )
            }
        ),
        (
            'User role',
            {
                'fields': (
                    'is_reader',
                    'is_staff',
                    'is_superuser',
                    'is_active',
                )
            }
        )
    )
    add_fieldsets = (
            None,
            {
                'fields': (
                    'email',
                    'password1',
                    'password2',
                )
            }
        ),
 
admin.site.register(Users, UsersAdmin)