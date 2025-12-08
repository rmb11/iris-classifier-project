from django.contrib import admin
from .models import PredictionMetadata


@admin.register(PredictionMetadata)
class PredictionMetadataAdmin(admin.ModelAdmin):
    """
    Admin configuration for viewing prediction metadata records.
    """
    list_display = ("created_at", "user", "file_name", "model_version", "result")
    list_filter = ("model_version", "user")
