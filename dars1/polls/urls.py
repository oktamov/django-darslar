from django.urls import path
from .views import homepage, questions

urlpatterns = [
    path('', homepage, name='homepage'),
    path('questions/', questions, name='questions'),
]


