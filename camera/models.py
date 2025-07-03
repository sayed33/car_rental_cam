from django.db import models

class Car(models.Model):
    car_type = models.CharField(max_length=100)
    car_number = models.CharField(max_length=100)
    image = models.ImageField(upload_to='cars/')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.car_type} - {self.car_number}"
