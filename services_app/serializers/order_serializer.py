from rest_framework.serializers import ModelSerializer

from services_app.models.order import Order

class OrderSlz(ModelSerializer):
    class Meta:
        model = Order
        fields = ('car', 'pickup_area', 'dropoff_area', 'pickup_date', 'pickup_time', 'dropoff_date',
                  'tariff', 'total_price', 'is_paid',  'is_shipped', 'is_repeated') # + car name, car key

class OrderBriefSlz(ModelSerializer):
    class Meta:
        model = Order
        fields = ('car', 'total_price', 'is_repeated')
        # car name, car key, total_price, is_repated
