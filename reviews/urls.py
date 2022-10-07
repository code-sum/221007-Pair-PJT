from django.urls import path
from . import views

app_name = 'reviews'

urlpatterns = [
    path('index/', views.index, name='index'),
]
