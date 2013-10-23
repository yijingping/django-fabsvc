from django.contrib import admin
from fabsvc.models import Group, Host, Service 

class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', )

class HostAdmin(admin.ModelAdmin):
    list_display = ('name', )

class ServiceAdmin(admin.ModelAdmin):
     list_display = ('name', 'path', 'host', 'group')

admin.site.register(Group, GroupAdmin)
admin.site.register(Host, HostAdmin)
admin.site.register(Service, ServiceAdmin)
