from django.contrib import admin
from apps.common.models import Social

@admin.register(Social)
class SocilAdmin(admin.ModelAdmin):
    list_display = ("title","social")
