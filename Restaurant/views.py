from django.shortcuts import render
from rest_framework import generics
from .models import MenuTable
from .serializers import MenuItemSerializer
from rest_framework import generics, viewsets
from .models import MenuTable, BookingTable

from .serializers import MenuItemSerializer, BookingSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes


class MenuItemsView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = MenuTable.objects.all()
    serializer_class = MenuItemSerializer


class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuTable.objects.all()
    serializer_class = MenuItemSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = BookingTable.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

