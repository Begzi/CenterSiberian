from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Type, New
from .serializers import *
from rest_framework import status, generics

# Create your views here.
class TypeApiListCreate(generics.ListCreateAPIView):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer

class TypeApiUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer


class NewApiListCreate(generics.ListCreateAPIView):
    queryset = New.objects.all()
    serializer_class = NewSerializer


class NewApiUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = New.objects.all()
    serializer_class = NewSerializer


class NewApiShowWithTypeColor(generics.ListAPIView):
    queryset = New.objects.all()
    serializer_class = NewShowWithColorSerializer

class NewApiShowWithTypeColor(generics.ListAPIView):
    queryset = New.objects.all()
    serializer_class = NewShowWithColorSerializer

class NewApiShowWithType(APIView):

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not id:
            return Response({"error": "Method GET with ID not allowed"})

        try:
            instance = Type.objects.get(pk=pk)
        except:
            return Response({"error": "Такого Type не существует"})

        queryset = New.objects.filter(type=instance).all()

        serializer_for_reading = NewSerializer(
            instance=queryset,
            many=True
        )
        return Response(serializer_for_reading.data)

