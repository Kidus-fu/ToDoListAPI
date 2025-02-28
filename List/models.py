from django.db import models
from django.contrib.auth.models import User

class List(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    item = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"created by {self.created_by } {self.item} - {self.completed}"