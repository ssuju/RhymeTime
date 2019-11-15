from django.contrib import admin

from .models import Account


class AccountList(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone')
    list_filter = ('first_name', 'last_name')
    search_fields = ('first_name', )
    ordering = ['first_name']


admin.site.register(Account)
