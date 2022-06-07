from django.contrib import admin

from .models import Lead

@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Lead._meta.get_fields()]