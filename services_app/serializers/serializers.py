from rest_framework.serializers import ModelSerializer

from services_app.models.contact import Contact
from services_app.models.happy_client import HappyClients

class ContactSlz(ModelSerializer):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'subject', 'message', 'added_date' )

class HappyClientsSlz(ModelSerializer):
    class Meta:
        model = HappyClients
        fields = ('name', 'email', 'job', 'website', 'body', 'added_date')