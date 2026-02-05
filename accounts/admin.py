from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from core.models import Post
from .forms import RegisterForm, CustomUserChangeForm
from .models import User


class PostInline(admin.TabularInline):
    model = Post


class CustomUserAdmin(UserAdmin):
    add_form = RegisterForm
    form = CustomUserChangeForm
    model = User
    inlines = [PostInline]
    list_display = [
        "email",
        "username",
        "bio",
        "image",
        "is_staff",
        "is_active",
    ]
    fieldsets = [
        (
            None,
            {
                "fields": [
                    "email",
                    "username",
                    'password',
                    "bio",
                    "image",
                    "is_staff",
                    "is_active",
                ]
            },
        )
    ]


admin.site.register(User, CustomUserAdmin)
