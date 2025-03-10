from django.urls import path
from .views import FoodViewer

URL_BASE = 'api/v1/food'

urlpatterns = [
    path(f'{URL_BASE}/', FoodViewer.as_view(), name='food-category-viewer'),
]