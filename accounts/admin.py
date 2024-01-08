from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('username', 'first_name', 'last_name', 'age', 'is_admin', 'is_staff', 'is_superuser')

    list_editable = ('is_admin',)
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('age', )}), (None, {'fields': ('is_admin',)}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('age', )}), (None, {'fields': ('is_admin',)}),
    )


