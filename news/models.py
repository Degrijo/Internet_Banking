from django.db import models


class Articles(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateTimeField()
    post = models.TextField()

    def __str__(self):
        return self.title