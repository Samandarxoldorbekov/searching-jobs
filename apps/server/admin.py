from django.contrib import admin
from apps.server.models import ServerAdd

@admin.register(ServerAdd)
class ServerAdmin(admin.ModelAdmin):
    list_display =("server_name","region")