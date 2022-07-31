from rest_framework import generics

from services_app.models.happy_client import HappyClients
from services_app.models.contact import Contact
from services_app.serializers.serializers import HappyClientsSlz, ContactSlz

# permission va ordering qo'shish kerak
class HappyClintsList(generics.ListAPIView):
    model = HappyClients
    serializer_class = HappyClientsSlz
    queryset = HappyClients.objects.all()

class ContactView(generics.ListCreateAPIView):
    model = Contact
    serializer_class = ContactSlz
    queryset = Contact.objects.all()
