from django.db import models

class BlogCategory(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name

class Blog(models.Model):
    category = models.ManyToManyField(BlogCategory, related_name='blog')
    title =  models.CharField(max_length=500)
    snippet =  models.CharField(max_length=500)
    body = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = '-created_date'

class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comment')
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    website = models.URLField(max_length=100, null=True)
    body = models.TextField()
    added_date = models.DateTimeField(auto_now_add=True)

    is_reply = models.BooleanField(default=False)
    reply_comment = models.ForeignKey('self',
                                      on_delete=models.CASCADE,
                                      related_name='reply_comment',
                                      null=True)

    def __str__(self):
        return self.name

    #validatsiya yozish kerak
