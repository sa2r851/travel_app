from rest_framework import serializers
from .models import *
class WeddingSerializer(serializers.Serializer):
    class Meta:
        model = hall
        fields = "__all__"

class AddressSerializer(serializers.Serializer):
    class Meta:
        model = Destination
        fields =fields = ['dest', 'img']
