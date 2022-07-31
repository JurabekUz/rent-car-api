from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    subject = models.CharField(max_length=50)
    message = models.TextField()
    added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}, {self.subject}"

    class Meta:
        ordering = ('-added_date',)