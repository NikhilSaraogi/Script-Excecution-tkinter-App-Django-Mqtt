from django.db import models

class MqttLog(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    topic = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return f"{self.topic}: {self.message} :{self.timestamp}"
    
