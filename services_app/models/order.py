from accounts_app.models import CustomUser as User
from django.db import models

from .cars import Car

class Order(models.Model):

    Tariff = (
        ('hour', 'Hour'),
        ('day', 'Day'),
        ('month', 'Month')
    )

    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='myorder')
    car = models.ForeignKey(Car, on_delete=models.SET_NULL, null=True, related_name='order')
    pickup_area = models.CharField(max_length=200, default='Company/Company Branches')
    dropoff_area = models.CharField(max_length=200, default='Company/Company Branches', blank=True, null=True)
    pickup_date = models.DateField()
    pickup_time = models.DateTimeField(blank=True, null=True)
    dropoff_date = models.DateField()
    tariff = models.CharField(max_length=5, choices=Tariff, default='hour')
    total_price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Total Price')
    is_paid = models.BooleanField(default=False)
    is_shipped = models.BooleanField(default=False)
    is_repeated = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user} {self.car}"

    def mark_as_shipped(self):
        self.is_paid = True
        self.save()

    def mark_as_paid(self):
        self.is_shipped = True
        self.save()

    def mark_as_repeat(self):
        self.is_repeated = True
        self.save()

    def change_dropoff_date(self, value):
        self.dropoff_date=value
        self.save()


