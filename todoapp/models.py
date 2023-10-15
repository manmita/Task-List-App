from django.db import models
class TodoListItem(models.Model):
    content = models.TextField()
    day = models.TextField(default=None, blank=True, null=True)

