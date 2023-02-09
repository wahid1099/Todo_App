from django.db import models


class Todo(models.Model):
    text = models.CharField(max_length=200)
    task_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-task_created',)

    def __str__(self):
        return self.text
