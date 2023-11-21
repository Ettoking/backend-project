from django.shortcuts import render
from rest_framework import generics
from .models import MenuTable
from .serializers import MenuItemSerializer

# Create your views here.
class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuTable.objects.all()
    serializer_class = MenuItemSerializer


class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuTable.objects.all()
    serializer_class = MenuItemSerializer

