from django.contrib import admin
from .models.cars import *
from .models.contact import *
from .models.happy_client import *
from .models.order import *

admin.site.register(Car)
admin.site.register(CarPrice)
admin.site.register(CarReview)
admin.site.register(CarFeatures)
admin.site.register(Contact)
admin.site.register(HappyClients)
admin.site.register(Order)

