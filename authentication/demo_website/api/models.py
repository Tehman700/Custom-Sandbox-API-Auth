from django.db import models

class AdminMessage(models.Model):
    message = models.TextField()
    uploaded_at = models.DateTimeField(auto_now_add=True)

