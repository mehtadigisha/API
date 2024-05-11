from django.db import models

# Create your models here.

class Location(models.Model):
    locationName = models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.locationName
    
class Item(models.Model):
    itemName = models.CharField(max_length=100)
    data_added = models.DateTimeField(auto_now_add=True)
    item_location = models.ForeignKey(Location,on_delete=models.CASCADE)

    def __str__(self):
        return self.itemName