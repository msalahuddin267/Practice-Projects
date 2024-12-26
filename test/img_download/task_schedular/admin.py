from django.contrib import admin
from .models import CronJobControl

@admin.register(CronJobControl)
class CronJobControlAdmin(admin.ModelAdmin):
    list_display = ('is_active', 'interval')
