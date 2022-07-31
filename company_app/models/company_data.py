from django.db import models

class AboutCompany(models.Model):
    about = models.TextField()
    brif_info = models.CharField(max_length=512)
    year_exp = models.IntegerField(default=1)
    yotal_cars = models.IntegerField()
    customers = models.IntegerField(blank=True, null=True)
    total_branchs = models.IntegerField(blank=True, null=True)

class CompanyData(models.Model):
    location = models.CharField(max_length=256)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)

class SocialAccounts(models.Model):
    website = models.URLField(max_length=100, null=True, blank=True)
    twitter = models.URLField(max_length=100, null=True, blank=True)
    facebook = models.URLField(max_length=100, null=True, blank=True)
    telegram = models.URLField(max_length=100, null=True, blank=True)
    tiktok = models.URLField(max_length=100, null=True, blank=True)
    instagram = models.URLField(max_length=100, null=True, blank=True)