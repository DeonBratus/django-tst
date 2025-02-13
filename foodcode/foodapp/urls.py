from django.urls import path
from .views import FoodViewer

urlpatterns = [
    path('api/v1/food/', FoodViewer.as_view(), name='food-viewer'),
]