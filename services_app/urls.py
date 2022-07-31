from django.urls import path

from services_app.views.views import HappyClintsList, ContactView
from services_app.views.car_views import CarDataList, CarPricingList, CarDetailView, CarView
from services_app.views.order_view import ( OrderView, OrderDetailView, UserOrdersList,
            MarkAsShipped, MarkAsPaid, MarkAsRepeated, ChangeDropoffDate, GetNoRepeated
            )

urlpatterns = [
    path('happyclients/', HappyClintsList.as_view()),
    path('contact/', ContactView.as_view()),
    path('cars/',CarDataList.as_view()), # car _data_list
    path('pricing/', CarPricingList.as_view()),
    path('cars/<int:pk>/', CarDetailView.as_view()), #vith APIView
    path('orders/',OrderView.as_view()),
    path('user-orders/', UserOrdersList.as_view()),
    path('user-orders/<int:pk>/',OrderDetailView.as_view()),
    path('user-orders/<int:pk>/mark-as-shipped/',MarkAsShipped.as_view()),
    path('user-orders/<int:pk>/mark-as-paid/',MarkAsPaid.as_view()),
    path('user-orders/<int:pk>/mark-as-repeated/',MarkAsRepeated.as_view()),
    path('user-orders/<int:pk>/get-no-repeated/',GetNoRepeated.as_view()),
    path('user-orders/<int:pk>/change-dropoff-date/',ChangeDropoffDate.as_view()),

    path('car-detail/<int:pk>/', CarView.as_view(), name='car-detail' )# with generic view

]