from django.urls import path
from django.urls.resolvers import URLPattern
from .views import FoodAPI

urlpatterns = [
    path('food/', FoodAPI.as_view()),
    path('food/<int:id>', FoodAPI.as_view())
]