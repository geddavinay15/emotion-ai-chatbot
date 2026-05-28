from django.db import models

class Chat(models.Model):

    user_message = models.TextField()

    bot_response = models.TextField()

    detected_emotion = models.CharField(max_length=50)

    created_at = models.DateTimeField(auto_now_add=True)