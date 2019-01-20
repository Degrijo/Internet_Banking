from django.db import models


class Articles(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateTimeField()
    text = models.TextField()
    author = models.CharField(max_length=100, default="anonymous")

    def __str__(self):
        return self.title
