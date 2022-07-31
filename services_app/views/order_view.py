from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from services_app.models.order import Order
from services_app.serializers.order_serializer import OrderSlz, OrderBriefSlz
from services_app.serializers.cars_serializer import CarSlz, CarFeaturesSlz
from services_app.permissions import IsOwnerOrReadOnly

#search permission ordering filter
class OrderView(APIView):
    permission_classes = permissions.IsAdminUser
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['is_paid', 'is_shipped', 'is_repeated', 'tariff', 'car']
    search_fields = ['user', 'car', 'pickup_area', 'dropoff_area']
    ordering_fields = ['dropoff_date', 'total_price']

    def get(self, request, *args, **kwargs):
        orders = Order.objects.all()
        serializer = OrderBriefSlz(orders, many=True)
        return Response(data=serializer.data)

    '''def post(self, request, *args, **kwargs):
        serializer = OrderSlz(data=request.data)
        serializer.is_valid(raise_exception=True)
        #print('serializer : ', serializer.data)
        #serializer.initial_data['user'] = self.request.user
        print('12 :',self.request.user)
        print('aa :',request.user)
        serializer.save(user=self.request.user)
        print(serializer.initial_data)

        return Response(serializer.data, status=status.HTTP_201_CREATED)'''

class OrderDetailView(APIView):
    permission_classes = IsOwnerOrReadOnly
    def get(self, request, pk, *args, **kwargs):
        order = Order.objects.get(pk=pk)
        car = order.car
        car_features = car.features

        orderslz = OrderSlz(order)
        carslz = CarSlz(car)
        car_featuresslz = CarFeaturesSlz(car_features)
        return Response(data = {
            'order' : orderslz.data,
            'car' : carslz.data,
            'car_features' : car_featuresslz.data
        })

    def post(self, request, *args, **kwargs):
        serializer = OrderSlz(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=self.request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


#search permission ordering filter
class UserOrdersList(APIView):
    permission_classes = IsOwnerOrReadOnly
    def get(self, request, *args, **kwargs):
        pk = request.user.id
        orders = Order.objects.filter(user_id=pk)
        serializer = OrderSlz(orders, many=True)
        return Response(data=serializer.data)

class MarkAsShipped(APIView):
    permission_classes = IsOwnerOrReadOnly

    def get(self, request, pk, *args, **kwargs):
        order = Order.objects.get(pk=pk)
        is_shipped = order.is_shipped
        data = {
            'is_shipped': is_shipped
        }
        return Response(data=data)

    def patch(self, request, pk, *args, **kwargs):
        order = Order.objects.get(pk=pk)
        order.mark_as_shipped()
        serializer = OrderSlz(order)
        return Response(data=serializer.data)

class MarkAsPaid(APIView):
    permission_classes = permissions.IsAdminUser

    def get(self, request, pk, *args, **kwargs):
        order = Order.objects.get(pk=pk)
        is_paid = order.is_paid
        data = {
            'is_paid': is_paid
        }
        return Response(data=data)

    def patch(self, request, pk, *args, **kwargs):
        order = Order.objects.get(pk=pk)
        order.mark_as_paid()
        serializer = OrderSlz(order)
        return Response(data=serializer.data)

class MarkAsRepeated(APIView):
    permission_classes = permissions.IsAdminUser

    def get(self, request, pk, *args, **kwargs):
        order = Order.objects.get(pk=pk)
        is_repeated = order.is_repeated
        data = {
            'is_repeated': is_repeated
        }
        return Response(data=data)

    def patch(self, request, pk, *args, **kwargs):
        order = Order.objects.get(pk=pk)
        order.mark_as_repeat()
        serializer = OrderSlz(order)
        return Response(data=serializer.data)

class GetNoRepeated(APIView):
    permission_classes = permissions.IsAdminUser
    def get(self, request, *args, **kwargs):
        orders = Order.objects.filter(is_repeated=False)
        serializer = OrderSlz(orders, many=True)
        return Response(data=serializer.data)


class ChangeDropoffDate(APIView):
    permission_classes = IsOwnerOrReadOnly

    def get(self, request, pk, *args, **kwargs):
        order = Order.objects.get(pk=pk)
        date = order.dropoff_date
        data = {
            'dropoff_date': date
        }
        return Response(data=data)

    def patch(self, request, pk, *args, **kwargs):
        new_date = request.data.get('new_date')
        order = Order.objects.get(pk=pk)
        order.change_dropoff_date(new_date)
        serializer = OrderSlz(order)
        return Response(data=serializer.data)


