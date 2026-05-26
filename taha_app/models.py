from django.db import models

class Crop(models.Model):
    crop_name = models.CharField(max_length=100)
    planting_date = models.DateField()
    watering_date = models.DateField()
    fertilizer_date = models.DateField()
    harvest_date = models.DateField()

    def __str__(self):
        return self.crop_name
