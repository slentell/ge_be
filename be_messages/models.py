from curses.ascii import US
from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=100)
    
    def __str__(self):
        return self.username


class Message(models.Model):
    user_author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_author')
    user_recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_recipient')
    message = models.CharField(max_length=1000)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.message

