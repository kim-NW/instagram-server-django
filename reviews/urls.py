from django.urls import path
from .views import MyReview

urlpatterns = [
    path("", MyReview.as_view())
]
