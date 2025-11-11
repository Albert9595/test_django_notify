from django.db import models
from django.utils import timezone

class User(models.Model):
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=30, null=True, blank=True)
    telegram_id = models.CharField(max_length=64, null=True, blank=True)

    def __str__(self):
        return f'User {self.id}'

class Notification(models.Model):
    STATUS_CHOICES = [
        ('new','new'),
        ('sent','sent'),
        ('failed','failed'),
        ('partial','partial'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    message = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    attempts = models.IntegerField(default=0)
    last_error = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'Notif {self.id} to {self.user_id} ({self.status})'