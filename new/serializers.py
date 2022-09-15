
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.validators import UniqueTogetherValidator
from .models import Type, New


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ('name', 'color')

class NewSerializer(serializers.ModelSerializer):
    # typeName = serializers.CharField(source='type.name', max_length=15)
    # typeColor = serializers.CharField(source='type.color', max_length=15)
    class Meta:
        model = New
        fields = ('name', 'shortDescription', 'description', 'type')

class NewShowWithColorSerializer(serializers.ModelSerializer):
    typeName = serializers.CharField(source='type.name', max_length=15)
    typeColor = serializers.CharField(source='type.color', max_length=15)
    class Meta:
        model = New
        fields = ('name', 'shortDescription', 'description', 'typeName', 'typeColor')