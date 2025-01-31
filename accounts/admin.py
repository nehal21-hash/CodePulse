from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CpUser

class CpUserAdmin(UserAdmin):
    # Add custom fields to the list display
    list_display = ('username', 'email', 'CodeForcesID', 'CodeChefID', 'LeetCodeID', 'AtCoderID', 'SpojID', 'is_staff')

    # Add custom fields to the fieldsets (used for editing an existing user)
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('CodeForcesID', 'CodeChefID', 'LeetCodeID', 'AtCoderID', 'SpojID')}),
    )

    # Add custom fields to the add_fieldsets (used for creating a new user)
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {
            'classes': ('wide',),
            'fields': ('email','CodeForcesID', 'CodeChefID', 'LeetCodeID', 'AtCoderID', 'SpojID'),
        }),
    )

admin.site.register(CpUser, CpUserAdmin)


