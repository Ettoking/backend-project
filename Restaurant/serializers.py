from rest_framework import serializers
from .models import MenuTable, BookingTable



class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuTable
        fields = ('id', 'title', 'price', 'inventory')


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookingTable
        # fields = '__all__'
        fields = ('id', 'name', 'number_of_guests', 'reservation_date')
        