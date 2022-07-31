from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from services_app.models.cars import *

class CarSlz(ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'

class CarBriefDataSlz(ModelSerializer):
    class Meta:
        model = Car
        fields = ('company', 'model', 'image')

'''
class CarDataSlz(serializers.Serializer):
    company = serializers.CharField(max_length=50)
    model = serializers.CharField(max_length=50)
    image = serializers.ImageField()
    type = serializers.CharField(max_length=50)
    day_price =serializers.IntegerField()
'''

class CarBriefDataPriceSlz(ModelSerializer):
    car = CarBriefDataSlz()
    class Meta:
        model = CarPrice
        fields = ('day','car')


class CarPriceSlz(ModelSerializer):
    car = CarBriefDataSlz()
    class Meta:
        model = CarPrice
        fields = '__all__'

class CarFeaturesSlz(ModelSerializer):
    class Meta:
        model = CarFeatures
        fields = '__all__'

class CarReviewSlz(ModelSerializer):
    class Meta:
        model = CarReview
        fields = '__all__'

class Car_Slz(ModelSerializer):
    price = CarPriceSlz()
    features = CarFeaturesSlz()
    review = CarReviewSlz(many=True)
    class Meta:
        model = Car
        fields = '__all__'