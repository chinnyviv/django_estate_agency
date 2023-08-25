from django.contrib import admin
from . models import MyMessages

class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'pname', 'plocation', 'msg_date', 'agent_id')
    list_display_links = ('id', 'name')
    list_filter = ('agent_id',)
    search_fields = ('name',)
    list_per_page = 25


admin.site.register(MyMessages, MessageAdmin)
