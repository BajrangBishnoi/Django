from rest_framework import serializers
from .models import Contact

class Contactserializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['name', 'number', 'created_at', 'favourite', 'type']
        extra_kwargs = {
            'name': {'required': False},
            'number': {'required': False},
            'created_at': {'required': False},
            'favourite': {'required': False},
            'type': {'required': False},
        }


class AddContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['name', 'number', 'created_at', 'favourite', 'type']
        extra_kwargs = {
            'name': {'required': False},
            'number': {'required': False},
            'created_at': {'required': False},
            'favourite': {'required': False},
            'type': {'required': False},
        }
        