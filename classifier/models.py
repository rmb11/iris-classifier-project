from django.conf import settings
from django.db import models


class PredictionMetadata(models.Model):
    """
    Stores metadata for each prediction, including
    model details, user information, and results.
    """
    file_name = models.CharField(max_length=255, blank=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    model_version = models.CharField(max_length=50, default="v1")
    result = models.CharField(max_length=100)
    metrics = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.created_at} - {self.result}"