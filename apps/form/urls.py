from django.urls import path
from .views import ExtractInfoAPIView

urlpatterns = [
    path('extract-info/', ExtractInfoAPIView.as_view(), name='extract-info'),
]