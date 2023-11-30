from django.db import models

# Create your models here.
class BookingTable(models.Model): # this is the table name in the database 
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    number_of_guests = models.IntegerField()
    # bookingDate = models.DateField()
    reservation_date = models.DateField()

    def __str__(self): # this is used to display the title and price in the admin panel
        return f'{self.name} - {str(self.number_of_guests)}'

class MenuTable(models.Model): # this is the table name in the database 
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()

    def __str__(self): # this is used to display the title and price in the admin panel
        return f'{self.title} - {str(self.price)}' # this is used to display the title and price in the admin panel
    


