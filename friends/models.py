""" from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
 
RequestStatus = (
    ('requested': 'Requested'),
    ('accepted': 'accepted'),
    ('rejected': 'rejected'),
)
 

class Friend(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    friend = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friends')
    status = models.CharField(max_length=20, default='requested')
    created_at = models.DateTimeField(default=now)

class CustomNotification(models.Model):
    type = models.CharField(default='friend', max_length=30)
    recipient = models.ForeignKey(User, blank=False, related_name='notifications', on_delete=models.CASCADE)
    actor = models.ForeignKey(User, blank=False, related_name='notifications', on_delete=models.CASCADE)
    unread = models.BooleanField(default=True, blank=False, db_index=True)

    #recipient = models.ForeignKey(settings.AUTH_USER_MODEL, blank=False, related_name='notifications', on_delete=models.CASCADE)
    #actor = models.ForeignKey(settings.AUTH_USER_MODEL, blank=False, on_delete=models.CASCADE)

    verb = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    timestamp = models.DateTimeField(default=now, db_index=True)
    deleted = models.BooleanField(default=False, db_index=True)
    emailed = models.BooleanField(default=False, db_index=True)
 """