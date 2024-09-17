from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    done = models.BooleanField(
        default=False,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name
