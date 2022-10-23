from .models import *
from .serializers import *
from rest_framework.decorators import api_view
import django_filters
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics


@api_view(['GET'])
def address_list_api(request):
    all_address=Destination.objects.all()
    data=AddressSerializer(all_address,many=True).data
    return Response ({'data':data})

class hall_list_api(generics.ListAPIView):
    queryset = hall.objects.all()
    serializer_class = WeddingSerializer
    filters_backends=(DjangoFilterBackend,SearchFilter)
    filter_fields=('number','location')
    search_fields=('name')
