from django.db import models

class HappyClients(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    job = models.CharField(max_length=50)
    website = models.URLField(max_length=100, null=True, blank=True)
    body = models.TextField()
    added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name