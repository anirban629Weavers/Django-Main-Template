from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model


admin.site.site_header = "JOB - PORTAL"
admin.site.site_title = "FIND YOUR DREAM JOBS"
admin.site.index_title = "GOOD JOB | GOOD LIFE"


class CustomUserAdmin(UserAdmin):

    empty_value_display = "-empty-"
    list_display = (
        'email',
        'name',
        'is_active',
    )

    list_display_links = ('email', 'name',)
    list_filter = ('is_active',)
    list_editable = ('is_active',)
    search_fields = ('email', 'name')
    ordering = ('email',)
    exclude = ('last_login',)
    fieldsets = (
        ("Contact Info", {
            'fields': (
                'email',
                )
            }
         ),
        (
            'Personal Info',
            {
                'fields': (
                    'name', 'image'
                ),
                "classes": ["wide", "extrapretty"],
            },
        ),
        (
            'Permissions', {
                'fields': (
                    'is_active', 'is_staff', 'is_superuser', 'groups',
                    )
                }
        ),
        (
            'Password', {
                'fields': (
                    'password',
                    )
                }
        ),
    )
    add_fieldsets = (
        (
            'Personal Info', {
                'fields': ('name',)
            }
        ),
        (
            'Contact Info', {
                'fields': ('email',),
            }
        ),
        (
            'Password', {
                'fields': ('password1', 'password2',),
            }
        ),
    )

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(is_superuser=False)


admin.site.register(get_user_model(), CustomUserAdmin)
