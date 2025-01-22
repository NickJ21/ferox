from django.urls import path
from .views import get_all_projects_list, contact_view

urlpatterns = [
    path('our_work/', get_all_projects_list, name="projects_list"),
    path('contact/', contact_view, name="contact")
]

