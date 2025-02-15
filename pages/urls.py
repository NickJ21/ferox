from django.urls import path
from .views import home, about, construction, agriculture, services

urlpatterns = [
    path("", home, name="home"),
    path("about/", about, name="about"),
    path("construction/", construction, name="construction"),
    path("agriculture/", agriculture, name="agriculture"),
    path("services/", services, name="services"),
]