from django.shortcuts import render, redirect
from .models import Car, CarImage
from django.utils import timezone

def camera_page(request):
    if request.method == 'POST':
        car_type = request.POST['car_type']
        car_number = request.POST['car_number']
        car = Car.objects.create(car_type=car_type, car_number=car_number)

        for file in request.FILES.getlist('images'):
            CarImage.objects.create(car=car, image=file, timestamp=timezone.now())

        return redirect('camera_page')

    return render(request, 'cars/camera.html')
