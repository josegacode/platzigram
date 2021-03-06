from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Models
from users.models import Profile
from django.contrib.auth.models import User

# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):

    # Which columns will be shown in the admin panel (theay are constant names)
    list_display = ("pk", "user", "phone_number", "website", "picture")
    list_display_links = ("pk", "user", "website", "picture")
    list_editable = ("phone_number",)

    # Shows a search field in admin panel by
    # using the given column filters
    search_fields = (
        "user__email",
        "user__username",
        "user__first_name",
        "user__last_name",
        "phone_number",
    )

    # Shows a sidebar column with this fields for filter
    list_filter = ("created", "modified", "user__is_active", "user__is_staff")

    # Customizing the fields which are shown in the edit
    # Profile section
    fieldsets = (
        # First set
        (
            "Profile",
            {
                # Each tuple of fields represents a row
                "fields": (("user", "picture"),),
            },
        ),
        # Second one
        ("Extra info", {"fields": (("website", "phone_number"), ("biography"))}),
        # Third one
        (
            "Metadata",
            {
                "fields": (("created", "modified"),),
            },
        ),
    )

    readonly_fields = (
        "created",
        "modified",
    )


class ProfileInline(admin.StackedInline):
    """Profile in-line admin for users."""

    model = Profile
    can_delete = False
    verbose_name_plural = "profiles"


class UserAdmin(BaseUserAdmin):
    """Add profile admin to base user admin."""

    inlines = (ProfileInline,)
    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        "is_active",
        "is_staff",
    )


admin.site.unregister(User)
admin.site.register(User, UserAdmin)