from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse

from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView
from .models import Item
from .serializers import ItemSerializer

class ItemListCreateView(ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class ItemRetrieveDeleteView(RetrieveDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer