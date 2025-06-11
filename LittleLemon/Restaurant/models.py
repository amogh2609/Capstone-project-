from django.db import models

# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length = 255 )
    no_of_guests = models.IntegerField(default = 1)
    booking_date = models.DateTimeField()

class Menu(models.Model):
    title = models.CharField(max_length = 255 , unique= True)
    price = models.DecimalField(max_digits=4 , decimal_places=2)
    inventory = models.IntegerField()
