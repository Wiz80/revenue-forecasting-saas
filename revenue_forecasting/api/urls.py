from django.urls import path
from .views import PrediccionRevenueView

urlpatterns = [
    path('prediction/', PrediccionRevenueView.as_view(), name='prediction-revenue'),
]
