from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from contactus.models import Contactus
from contactus.serializers import ContactUsSerializer
from rest_framework import status



class ContactUsSerializerAPIView(APIView):

    def get(self, request, *args, **kwargs):
        cont_obj = Contactus.objects.all()
        cont_ser_obj = ContactUsSerializer(cont_obj, many=True)
        return Response(cont_ser_obj.data)


    def post(self, request, *args, **kwargs):
        
        print(request.data)
        ser_obj = ContactUsSerializer(data = request.data)
        print(ser_obj)
        if ser_obj.is_valid():
            ser_obj.save()
            return render(request, template_name='index.html')
        return Response(ser_obj.errors, status = status.HTTP_400_BAD_REQUEST)
