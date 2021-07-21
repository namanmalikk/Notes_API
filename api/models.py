from django.db import models

# Create your models here.


class Note(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title[:30]

    class Meta:
        ordering = ['-updated']
