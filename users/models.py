from django.db import models
from django.utils import timezone

class User(models.Model):
    zoho_user_id = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    status = models.CharField(max_length=20, choices=[('active', 'Active'), ('deactivated', 'Deactivated')])
    access_type = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class UserLog(models.Model):
    user = models.ForeignKey(User, related_name='logs', on_delete=models.CASCADE)
    event_type = models.CharField(max_length=20, choices=[('activation', 'Activation'), ('deactivation', 'Deactivation')])
    event_timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.name} - {self.event_type} at {self.event_timestamp}"
