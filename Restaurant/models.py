from django.db import models

# Create your models here.
class BookingTable(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    number_of_guests = models.IntegerField()
    bookingDate = models.DateTimeField()


class MenuTable(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()