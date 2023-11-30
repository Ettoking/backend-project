
from .models import BookingTable
from django import forms



class BookingTableForm(forms.ModelForm):
    class Meta:
        model = BookingTable
        fields = '__all__'