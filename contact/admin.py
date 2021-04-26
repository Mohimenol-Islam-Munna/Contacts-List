from django.contrib import admin
from .models import Contact


admin.site.register(Contact)

# @admin.register(Contact)
# class ContactAdmin(admin.ModelAdmin):
#     list_display = ('full_name', 'email', 'relationship',
#                     'phone-number', 'address')
