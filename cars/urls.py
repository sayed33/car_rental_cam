from django.urls import path
from . import views

urlpatterns = [
    path('', views.camera_page, name='camera_page'),
]
