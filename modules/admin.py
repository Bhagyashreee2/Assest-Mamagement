from django.contrib import admin
from modules.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import CustomUserCreationForm

class UserModelAdmin(BaseUserAdmin):
    # The fields to be used in displaying the UserModelAdmin.
    # These override the definitions on the base UserModelAdmin
    # that reference specific fields on auth.User.
    list_display = ("id", "Email", "First_Name", "Last_Name", "is_admin")
    list_filter = ("is_admin",)
    fieldsets = (
        ("User Credentials", {"fields": ("Email", "password")}),
        ("Personal info", {"fields": ("First_Name", "Last_Name", "Terms_Privacy_Policy")}),
        ("Permissions", {"fields": ("is_admin",)}),
        
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("Email", "First_Name", "Last_Name", "Terms_Privacy_Policy", "password", "Re_type_Your_password"),
            }
        ),
    )
    search_fields = ("Email",)
    ordering = ("Email", "id")
    filter_horizontal = ()

    # add_form = CustomUserCreationForm


# Now register the new UserAdmin...
admin.site.register(User, UserModelAdmin)
# admin.site.register(User)
