from django.db import models

class Car(models.Model):
    company = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/car/')
    type = models.CharField(max_length=50)
    transmission = models.CharField(max_length=50)
    seats = models.PositiveIntegerField()
    luggage = models.PositiveIntegerField()
    fuel = models.CharField(max_length=50)
    description = models.TextField()
    key = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.company} {self.model}"

class CarPrice(models.Model):
    car = models.OneToOneField(Car, on_delete=models.CASCADE, related_name='price')
    mileage = models.IntegerField()
    hour = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Per Hour Rate')
    day = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Per Day Rate')
    month = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Per Month Rate')
    hour_surch = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Per Hour Rate')
    day_surch= models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Per Day Rate')

    def __str__(self):
        return f"{self.car.company} {self.car.model} day:{self.day}"

class CarFeatures(models.Model):
    car = models.OneToOneField(Car, on_delete=models.CASCADE, related_name='features')
    airconditions = models.BooleanField(default=False)
    child_seat = models.BooleanField(default=False)
    gps = models.BooleanField(default=False)
    luggage = models.BooleanField(default=False)
    black_window = models.BooleanField(default=False)
    seat_belt = models.BooleanField(default=False)
    sleeping_bed = models.BooleanField(default=False)
    water = models.BooleanField(default=False)
    bluetooth = models.BooleanField(default=False)
    onboard_computer = models.BooleanField(default=False)
    Audio_input = models.BooleanField(default=False)
    long_term_trips = models.BooleanField(default=False)
    car_kit = models.BooleanField(default=False)
    remote_central_locking = models.BooleanField(default=False)
    climate_control = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.car.company} {self.car.model}"

class CarReview(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='review')
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    website = models.URLField(max_length=100, null=True, blank=True)
    rate = models.PositiveSmallIntegerField()
    body = models.TextField()
    added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.car.company} {self.car.model} "

