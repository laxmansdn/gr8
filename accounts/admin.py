from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account
# Register your models here.

class AccountAdmin(UserAdmin):
    list_display = ('first_name', 'last_name', 'username', 'email', 'last_login', 'date_of_join', 'is_active',)
    list_display_links = ('first_name', 'last_name', 'username', 'email',)
    readonly_fields = ('date_of_join', 'last_login',)
    ordering = ('-date_of_join',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Account, AccountAdmin)
