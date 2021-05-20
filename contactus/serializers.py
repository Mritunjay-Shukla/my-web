from rest_framework import serializers
from contactus.models import Contactus





class ContactUsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Contactus
        fields = ('id', 'name', 'subject', 'phone', 'email', 'description')

