from django.db import models
from django.utils import timezone

# Create your models here.

class Message(models.Model):
    user = models.CharField(max_length=60)
    content = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return f'{self.user}: {self.content} at {self.time}'
    
    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()
        return f'{self.user}: {self.content} deleted at {self.deleted_at}'
    

class Room(models.Model):
    name = models.CharField(max_length=100, unique=True)
    id = models.IntegerField(primary_key=True)
    status = models.CharField(max_length=20, default='active')
    
    def __str__(self):
        return self.name
    
    def deactivate(self):
        self.status = 'inactive'
        self.save()
        return f'Room {self.name} is now inactive'
    
class ChatUser(models.Model):
    username = models.CharField(max_length=60)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    is_active = models.BooleanField(default=True)
    joined_at = models.DateTimeField(auto_now_add=True)
    last_seen = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.username

    def deactivate(self):
        self.is_active = False
        self.save()
        return f'User {self.username} is now inactive'

    def update_last_seen(self):
        self.last_seen = timezone.now()
        self.save()
        return f'User {self.username} last seen updated to {self.last_seen}'

    def date_joined(self):
        return f'User {self.username} joined at {self.joined_at}'
    