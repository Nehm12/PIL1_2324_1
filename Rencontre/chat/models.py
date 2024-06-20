from datetime import timezone
from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.

class list_user(models.Model):
    list= models.ManyToManyField(User)
    
    def __str__(self):
        return self.list.username
    

class Message(models.Model):
    newroom = models.ForeignKey(list_user, on_delete=models.CASCADE) 
    user1 = models.ForeignKey(User, on_delete=models.CASCADE,related_name='messages_sent')
    user2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='messages_received')
    content = models.TextField()
    timestamp=models.DateTimeField(default=now)
    
    def __str__(self):
        return f"{self.user2.username}: {self.content[:50]}"
    

    
    
