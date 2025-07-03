
from django.db import models

class Car(models.Model):
    car_type = models.CharField(max_length=100)
    car_number = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

class CarImage(models.Model):
    car = models.ForeignKey(Car, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='car_images/')
    timestamp = models.DateTimeField(auto_now_add=True)
