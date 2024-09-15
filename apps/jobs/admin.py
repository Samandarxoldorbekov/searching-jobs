from django.contrib import admin
from apps.jobs.models import JobsAdd

@admin.register(JobsAdd)
class AdminJobs(admin.ModelAdmin):
    list_display =("jobs_name","jobs_term","salary","diplom")
