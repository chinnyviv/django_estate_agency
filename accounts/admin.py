from django.contrib import admin
from . models import Users

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'fullname', 'email', 'phone', 'reg_date')
    list_display_links = ('id', 'fullname')
    list_filter = ('reg_date',)
    search_fields = ('fullname',)
    list_per_page = 25


admin.site.register(Users, UserAdmin)