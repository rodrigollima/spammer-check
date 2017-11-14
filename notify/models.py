from django.db import models
import uuid


class Notify(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sender  = models.CharField(blank=False, max_length=256)
    subject = models.TextField(blank=False)
    message = models.TextField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    authorize = models.BooleanField(default=False)
    count = models.IntegerField(default=0)

    class Meta:
        ordering = ('created_at',)  