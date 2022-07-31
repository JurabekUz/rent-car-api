from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.pagination import LimitOffsetPagination
from rest_framework import filters

from services_app.models.cars import Car, CarReview, CarPrice, CarFeatures
from services_app.serializers.cars_serializer import ( CarSlz, CarPriceSlz, CarReviewSlz,
                                                       CarFeaturesSlz, CarBriefDataPriceSlz, Car_Slz)

# cars haqidagi qisqacha malumotlar
# pagination qoshish kk
class CarDataList(APIView):
    pagination_class = LimitOffsetPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['car']

    def get(self, request, *args,**kwargs):
        #cars = Car.objects.all()
        car_price = CarPrice.objects.all()
        serializer = CarBriefDataPriceSlz(car_price, many=True)
        return Response(data=serializer.data)

#car ning batafsil narxlari
class CarPricingList(APIView):
    def get(self, request, *args, **kwargs):
        #cars = Car.objects.all()
        prices = CarPrice.objects.all()
        serializer = CarPriceSlz(prices, many=True)
        return Response(data=serializer.data)

# car detail da car price ishlatilmydi
class CarDetailView(APIView):
    def get(self, request, pk, *args, **kwargs):
        #ayni carni olish
        car = Car.objects.get(pk=pk)

        #ayni carning malumotlarini car id orqali olish
        car_price = CarPrice.objects.get(car=pk)
        car_feature = CarFeatures.objects.get(car=pk)
        car_reviews = CarReview.objects.filter(car=pk)

        # ayni car malumotlarini related_name orqali olish
        mileage = car.price.mileage
        feature = car.features
        review = car.review

        car_slz = CarSlz(car)
        features_slz = CarFeaturesSlz(feature)
        reviews_slz = CarReviewSlz(review, many=True)

        return Response(data={
            'mileage': mileage,
            'car': car_slz.data,
            'features': features_slz.data,
            'reviews': reviews_slz.data
        }, status=200)

        # annotate ishlatish kerak

class CarView(RetrieveAPIView):
    serializer_class = Car_Slz
    #queryset = Car.objects.all()
    queryset = Car.objects.prefetch_related('price', 'features', 'review').all()